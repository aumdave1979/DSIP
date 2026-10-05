import cv2
import numpy as np
from google.colab.patches import cv2_imshow


# ============================================================
# Apply Median Filter
# ============================================================

def apply_median_filter(image, kernel_size):
    # Apply median filter to remove noise
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image


# ============================================================
# Apply Bilateral Filter
# ============================================================

def apply_bilateral_filter(image, d, sigma_color, sigma_space):
    # Apply bilateral filter to remove noise while preserving edges
    filtered_image = cv2.bilateralFilter(
        image,
        d,
        sigma_color,
        sigma_space
    )
    return filtered_image


# ============================================================
# Load the input image
# ============================================================

image_path = "/content/aum.jpeg"

input_image = cv2.imread(image_path)

if input_image is None:
    print("Error: Could not load the image.")
    print("Check whether 'imagebright.png' exists in the current folder.")
    exit()
# ============================================================
# Apply Median Filter
# ============================================================

median_filtered_image = apply_median_filter(
    input_image,
    kernel_size=5
)
# ============================================================
# Apply Bilateral Filter
# ============================================================

bilateral_filtered_image = apply_bilateral_filter(
    input_image,
    d=9,
    sigma_color=75,
    sigma_space=75
)


# ============================================================
# Resize images
# ============================================================

width = 400
height = 300

original_resized = cv2.resize(
    input_image,
    (width, height)
)

median_resized = cv2.resize(
    median_filtered_image,
    (width, height)
)

bilateral_resized = cv2.resize(
    bilateral_filtered_image,
    (width, height)
)


# ============================================================
# Combine images horizontally
# ============================================================

combined_image = np.hstack(
    (
        original_resized,
        median_resized,
        bilateral_resized
    )
)


# ============================================================
# Display result in Google Colab
# ============================================================

cv2_imshow(combined_image)


# ============================================================
# Save filtered images
# ============================================================

median_filtered_path = "median_filtered_image.jpg"
bilateral_filtered_path = "bilateral_filtered_image.jpg"

cv2.imwrite(
    median_filtered_path,
    median_filtered_image
)

cv2.imwrite(
    bilateral_filtered_path,
    bilateral_filtered_image
)


# ============================================================
# Print saved file paths
# ============================================================

print(
    "Median filtered image saved at:",
    median_filtered_path
)

print(
    "Bilateral filtered image saved at:",
    bilateral_filtered_path
)