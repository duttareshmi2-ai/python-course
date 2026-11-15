import cv2
import numpy as np

# --------------------------------------------------
# DETECTION CONFIDENCE LAB
# --------------------------------------------------

def analyze_detections(frame, boxes, objectness, class_scores, class_names):
    """
    boxes:        (N,4) [x,y,w,h]
    objectness:   (N,)
    class_scores: (N,C)
    """

    # Part 1
    scores = objectness[:, np.newaxis] * class_scores

    # Part 2
    best_class = np.argmax(scores, axis=1)
    best_score = np.max(scores, axis=1)

    thresholds = [0.30, 0.50, 0.70]

    print("\n========== DETECTION REPORT ==========")

    for threshold in thresholds:

        keep = best_score >= threshold

        kept_count = np.sum(keep)

        print(f"Threshold {threshold:.2f}: {kept_count} detections kept")

    print("======================================\n")

    output = frame.copy()

    for i in range(len(boxes)):

        if best_score[i] < 0.50:
            continue

        x, y, w, h = boxes[i]

        confidence = best_score[i]
        class_id = best_class[i]
        class_name = class_names[class_id]

        color = (
            int((37 * class_id) % 255),
            int((67 * class_id) % 255),
            int((97 * class_id) % 255)
        )

        cv2.rectangle(
            output,
            (x, y),
            (x + w, y + h),
            color,
            2
        )

        label = f"{class_name} {confidence:.2f}"

        cv2.putText(
            output,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

        # Confidence bar
        bar_width = int(150 * confidence)

        cv2.rectangle(
            output,
            (x, y + h + 10),
            (x + 150, y + h + 25),
            (60, 60, 60),
            -1
        )

        cv2.rectangle(
            output,
            (x, y + h + 10),
            (x + bar_width, y + h + 25),
            color,
            -1
        )

    return output


# Example data

frame = np.zeros((720, 1280, 3), dtype=np.uint8)

boxes = np.array([
    [100, 100, 200, 150],
    [450, 180, 180, 220],
    [800, 120, 160, 160]
])

objectness = np.array([0.90, 0.75, 0.85])

class_scores = np.array([
    [0.10, 0.85, 0.20],
    [0.75, 0.10, 0.25],
    [0.15, 0.30, 0.95]
])

class_names = [
    "Person",
    "Car",
    "Dog"
]

result = analyze_detections(
    frame,
    boxes,
    objectness,
    class_scores,
    class_names
)

cv2.imshow("Detection Confidence Lab", result)
cv2.waitKey(0)
cv2.destroyAllWindows()