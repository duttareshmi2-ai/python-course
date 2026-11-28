import cv2
import onnxruntime as ort
import numpy as np
import math

# -----------------------------
# PART 1: Get only confident points
# -----------------------------
CONF_THRESHOLD = 0.5

KEYPOINT_NAMES = [
    "nose",
    "left_eye", "right_eye",
    "left_ear", "right_ear",
    "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow",
    "left_wrist", "right_wrist"
]

def extract_keypoints(raw_keypoints):
    points = {}

    for name, kp in zip(KEYPOINT_NAMES, raw_keypoints):
        x, y, conf = kp

        if conf >= CONF_THRESHOLD:
            points[name] = (x, y)

    return points


# -----------------------------
# PART 2: Convert arm points to angles
# -----------------------------
def calc_angle(p1, p2):
    return math.degrees(
        math.atan2(
            p2[1] - p1[1],
            p2[0] - p1[0]
        )
    )


def get_arm_angles(points):

    required = [
        "left_shoulder",
        "left_elbow",
        "left_wrist",
        "right_shoulder",
        "right_elbow",
        "right_wrist"
    ]

    if not all(part in points for part in required):
        return None

    return {
        "left_upper":
            calc_angle(points["left_shoulder"],
                       points["left_elbow"]),

        "left_lower":
            calc_angle(points["left_elbow"],
                       points["left_wrist"]),

        "right_upper":
            calc_angle(points["right_shoulder"],
                       points["right_elbow"]),

        "right_lower":
            calc_angle(points["right_elbow"],
                       points["right_wrist"])
    }


# -----------------------------
# PART 3: Compare with T-pose
# -----------------------------
def shortest_angle_difference(a, b):
    diff = abs(a - b)
    return min(diff, 360 - diff)


def score_t_pose(angles):

    t_pose = {
        "left_upper": 180,
        "left_lower": 180,
        "right_upper": 0,
        "right_lower": 0
    }

    scores = []

    for key in t_pose:

        diff = shortest_angle_difference(
            angles[key],
            t_pose[key]
        )

        score = max(0, 100 - diff)
        scores.append(score)

    return sum(scores) / len(scores)


# -----------------------------
# PART 4: Best frame = PASS / TRY AGAIN
# -----------------------------
best_score = 0

# Load ONNX pose model
session = ort.InferenceSession(
    "pose_estimation.onnx",
    providers=["CPUExecutionProvider"]
)

cap = cv2.VideoCapture("video.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Example preprocessing
    img = cv2.resize(frame, (256, 256))
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, 0)

    # Run ONNX model
    output = session.run(
        None,
        {session.get_inputs()[0].name: img}
    )[0]

    # Example:
    # shape (11,3)
    keypoints = output[0]

    # PART 1
    points = extract_keypoints(keypoints)

    # Draw confident points
    for x, y in points.values():
        cv2.circle(
            frame,
            (int(x), int(y)),
            5,
            (0, 255, 0),
            -1
        )

    # PART 2
    angles = get_arm_angles(points)

    if angles is not None:

        # PART 3
        score = score_t_pose(angles)

        if score > best_score:
            best_score = score

        cv2.putText(
            frame,
            f"Score: {score:.1f}%",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    cv2.imshow("T-Pose Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# PART 4
print(f"Best Score: {best_score:.2f}%")

if best_score >= 80:
    print("PASS")
else:
    print("TRY AGAIN")