import cv2
import numpy as np
from segment_anything import sam_model_registry, SamPredictor

# ----------------------------------
# 1. Load image
# ----------------------------------
image = cv2.imread("apple.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ----------------------------------
# 2. Load SAM model
# ----------------------------------
sam_checkpoint = "sam_vit_b.pth"
model_type = "vit_b"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
predictor = SamPredictor(sam)
predictor.set_image(image_rgb)

# ----------------------------------
# 3. Collect clicks
# ----------------------------------
clicked_points = []
clicked_labels = []  # 1 = apple, 0 = not apple

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append([x, y])
        clicked_labels.append(1)
        print(f"Apple point: ({x}, {y})")

    elif event == cv2.EVENT_RBUTTONDOWN:
        clicked_points.append([x, y])
        clicked_labels.append(0)
        print(f"Not apple point: ({x}, {y})")

display = image.copy()
cv2.namedWindow("Click Apple")
cv2.setMouseCallback("Click Apple", mouse_click)

print("Left Click = Apple")
print("Right Click = Background")
print("Press ENTER when done")

while True:
    cv2.imshow("Click Apple", display)
    key = cv2.waitKey(1)

    if key == 13:  # Enter key
        break

cv2.destroyAllWindows()

# ----------------------------------
# 4. Convert clicks into SAM prompts
# ----------------------------------
input_points = np.array(clicked_points)
input_labels = np.array(clicked_labels)

# --------------------
# 5. Get SAM's 3 mask guesses
# ----------------------------------
masks, scores, logits = predictor.predict(
    point_coords=input_points,
    point_labels=input_labels,
    multimask_output=True
)

# ----------------------------------
# 6. Sort masks from smallest to largest
# ----------------------------------
mask_sizes = [np.sum(mask) for mask in masks]
sorted_indices = np.argsort(mask_sizes)

sorted_masks = masks[sorted_indices]

# ----------------------------------
# 7. Choose largest mask (whole apple)
# ----------------------------------
apple_mask = sorted_masks[-1]

# ----------------------------------
# 8. Resize mask to photo size
# ----------------------------------
apple_mask = apple_mask.astype(np.uint8) * 255

apple_mask = cv2.resize(
    apple_mask,
    (image.shape[1], image.shape[0]),
    interpolation=cv2.INTER_NEAREST
)

# ----------------------------------
# 9. Create transparent sticker
# ----------------------------------
b, g, r = cv2.split(image)

rgba = cv2.merge([
    b,
    g,
    r,
    apple_mask
])

# ----------------------------------
# 10. Save sticker
# ----------------------------------
cv2.imwrite("apple_sticker.png", rgba)

print("Sticker saved as apple_sticker.png")