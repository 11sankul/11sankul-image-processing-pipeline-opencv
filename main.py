import cv2
import numpy as np
import os
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

file_path = "input_image.jpeg"
print(f"Looking for: {file_path}")
print("Current directory:", os.getcwd())
print("Files here:", os.listdir())

if not os.path.exists(file_path):
    print("ERROR: File does not exist!")
else:
    image = cv2.imread(file_path)
    if image is None:
        print("ERROR: OpenCV couldn't read the image (may be corrupted or unsupported format).")
    else:
        print("Image loaded successfully.")


# 1. Convert to Grayscale
def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Resize Image (Shrink or Stretch)
def resize_image(img, fx=0.5, fy=0.5):
    return cv2.resize(img, (0, 0), fx=fx, fy=fy)

# 3. Apply Gaussian Blur
def apply_gaussian_blur(img, kernel_size=(15, 15)):
    return cv2.GaussianBlur(img, kernel_size, 0)

# 4. Adjust Contrast using HSV
def adjust_contrast_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])  # Adjust brightness/contrast
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 5. Remove Red Color using HSV Masking
def remove_red_color(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    return cv2.bitwise_and(img, img, mask=cv2.bitwise_not(red_mask))

# === MAIN PIPELINE ===
def main():
    # Load Image
    img = cv2.imread("input_image.jpg")
    if img is None:
        print("Error: input_image.jpeg not found.")
        return

    # Original Image
    cv2.imshow("Original", img)
    cv2.waitKey(0)

    # Grayscale
    gray = convert_to_grayscale(img)
    cv2.imshow("Grayscale", gray)
    cv2.imwrite("output_grayscale.jpg", gray)
    cv2.waitKey(0)

    # Resize (Shrink and then Stretch)
    shrink = resize_image(img, fx=0.5, fy=0.5)
    stretch = resize_image(shrink, fx=2.0, fy=2.0)
    cv2.imshow("Stretched Image", stretch)
    cv2.imwrite("output_stretched.jpg", stretch)
    cv2.waitKey(0)

    # Gaussian Blur
    blurred = apply_gaussian_blur(img)
    cv2.imshow("Gaussian Blur", blurred)
    cv2.imwrite("output_blur.jpg", blurred)
    cv2.waitKey(0)

    # Contrast Adjustment (HSV)
    contrast = adjust_contrast_hsv(img)
    cv2.imshow("Contrast Adjusted (HSV)", contrast)
    cv2.imwrite("output_contrast.jpg", contrast)
    cv2.waitKey(0)

    # Red Color Removal
    no_red = remove_red_color(img)
    cv2.imshow("Red Removed", no_red)
    cv2.imwrite("output_no_red.jpg", no_red)
    cv2.waitKey(0)

    # Clean up windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
