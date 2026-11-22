import cv2
import numpy as np

# -----------------------------
# Load images
# -----------------------------
student = cv2.imread("student.png")
matte = cv2.imread("matte.png", cv2.IMREAD_GRAYSCALE)
blue_card = cv2.imread("blue_card.jpg")

# Convert matte from 0-255 to 0-1
matte_float = matte / 255.0

# ==================================================
# PART 1: Count sure, unsure and room pixels
# ==================================================
sure_pixels = np.sum(matte_float > 0.95)
unsure_pixels = np.sum((matte_float > 0.05) & (matte_float < 0.95))
room_pixels = np.sum(matte_float <= 0.05)

print("Sure pixels:", sure_pixels)
print("Unsure pixels:", unsure_pixels)
print("Room pixels:", room_pixels)

# ==================================================
# PART 2: Keep only biggest patch and fill it
# ==================================================
binary = (matte_float > 0.5).astype(np.uint8)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    binary,
    connectivity=8
)

largest_label = 1
largest_area = 0

for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]

    if area > largest_area:
        largest_area = area
        largest_label = i

clean_mask = np.zeros_like(binary)
clean_mask[labels == largest_label] = 255

# Fill holes
kernel = np.ones((15, 15), np.uint8)
clean_mask = cv2.morphologyEx(
    clean_mask,
    cv2.MORPH_CLOSE,
    kernel
)

# ==================================================
# PART 3: Paste student onto blue card
# ==================================================
h, w = blue_card.shape[:2]

student = cv2.resize(student, (w, h))
clean_mask = cv2.resize(clean_mask, (w, h))

alpha = clean_mask.astype(np.float32) / 255.0
alpha = np.stack([alpha, alpha, alpha], axis=2)

result = (
    student.astype(np.float32) * alpha +
    blue_card.astype(np.float32) * (1 - alpha)
)

result = result.astype(np.uint8)

# ==================================================
# PART 4: Compare face using raw and cleaned matte
# ==================================================
raw_alpha = cv2.resize(matte_float, (w, h))
raw_alpha = np.stack([raw_alpha, raw_alpha, raw_alpha], axis=2)

raw_blend = (
    student.astype(np.float32) * raw_alpha +
    blue_card.astype(np.float32) * (1 - raw_alpha)
)

raw_blend = raw_blend.astype(np.uint8)

cv2.imshow("Raw Matte Blend", raw_blend)
cv2.imshow("Clean Matte Blend", result)

cv2.imwrite("raw_blend.jpg", raw_blend)
cv2.imwrite("clean_blend.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()