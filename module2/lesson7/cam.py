

import argparse
from pathlib import Path

import cv2


def adjust_brightness(image, value):
	"""Increase or decrease brightness while keeping valid pixel values."""
	return cv2.convertScaleAbs(image, alpha=1.0, beta=value)


def main():
	parser = argparse.ArgumentParser(description="Perform basic image edits with OpenCV")
	parser.add_argument("image", help="Path to the input image")
	parser.add_argument("--brightness", type=int, default=40,
						help="Brightness adjustment (-255 to 255)")
	args = parser.parse_args()

	image = cv2.imread(args.image)
	if image is None:
		raise FileNotFoundError(f"Could not read image: {args.image}")

	height, width = image.shape[:2]

	# Flip horizontally (basic image manipulation).
	flipped = cv2.flip(image, 1)

	# Rotate 90 degrees clockwise.
	rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

	# Crop the center half of the image.
	y_start, y_end = height // 4, 3 * height // 4
	x_start, x_end = width // 4, 3 * width // 4
	cropped = image[y_start:y_end, x_start:x_end]

	brightened = adjust_brightness(image, args.brightness)

	output_dir = Path("opencv_output")
	output_dir.mkdir(exist_ok=True)
	cv2.imwrite(str(output_dir / "flipped.jpg"), flipped)
	cv2.imwrite(str(output_dir / "rotated.jpg"), rotated)
	cv2.imwrite(str(output_dir / "cropped.jpg"), cropped)
	cv2.imwrite(str(output_dir / "brightness_adjusted.jpg"), brightened)
	print(f"Saved edited images to: {output_dir.resolve()}")


if __name__ == "__main__":
	main()
