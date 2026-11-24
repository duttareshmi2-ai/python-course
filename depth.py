import cv2
import numpy as np

# Load depth map as grayscale image
depth = cv2.imread("depth_map.png", cv2.IMREAD_GRAYSCALE)

if depth is None:
    print("Depth map not found!")
    exit()

# --------------------------------------------------
# Part 1: Normalise depth values (0 = far, 1 = near)
# --------------------------------------------------
depth_norm = depth.astype(np.float32) / 255.0

# Invert if lighter pixels are nearer
depth_norm = 1.0 - depth_norm

# --------------------------------------------------
# Part 2: Find closest obstacle and determine side
# --------------------------------------------------
h, w = depth_norm.shape

# Threshold for near objects
near_mask = depth_norm > 0.7

if np.any(near_mask):
    x_positions = np.where(near_mask)[1]
    avg_x = np.mean(x_positions)

    if avg_x < w / 3:
        side = "LEFT"
    elif avg_x < 2 * w / 3:
        side = "CENTER"
    else:
        side = "RIGHT"

    print("Obstacle detected on:", side)
else:
    print("No nearby obstacle detected")

# --------------------------------------------------
# Part 3: Create parallax wobble effect
# --------------------------------------------------
near_shift = 10
far_shift = 3

wobble = np.zeros_like(depth)

for y in range(h):
    for x in range(w):
        shift = int(
            far_shift +
            (near_shift - far_shift) * depth_norm[y, x]
        )

        new_x = min(w - 1, x + shift)
        wobble[y, new_x] = depth[y, x]

# --------------------------------------------------
# Part 4: Compare relative depth
# --------------------------------------------------
depth_big = depth_norm * 3.0

# Renormalise
depth_big = (depth_big - depth_big.min()) / (
    depth_big.max() - depth_big.min() + 1e-6
)

difference = np.mean(np.abs(depth_big - depth_norm))

print("Relative depth difference:", round(difference, 4))

# --------------------------------------------------
# Display
# --------------------------------------------------
cv2.imshow("Original Depth", depth)
cv2.imshow("Normalised Depth", depth_norm)
cv2.imshow("Parallax Wobble", wobble)

cv2.waitKey(0)
cv2.destroyAllWindows()