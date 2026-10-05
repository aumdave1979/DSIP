import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/content/aum.jpeg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================================================
# 1. Gaussian Smoothing
# ============================================================

kernel_size = (5, 5)
sigma = 1.5

# Create 1D Gaussian kernel
gaussian_kernel_1d = cv2.getGaussianKernel(5, sigma)

# Convert 1D kernel into 2D kernel
gaussian_kernel = np.outer(
    gaussian_kernel_1d,
    gaussian_kernel_1d
)

print("Gaussian Kernel:")
print(gaussian_kernel)

# Apply Gaussian smoothing
smoothed_image = cv2.filter2D(
    image,
    -1,
    gaussian_kernel
)

# Convert BGR to RGB
smoothed_rgb = cv2.cvtColor(
    smoothed_image,
    cv2.COLOR_BGR2RGB
)

# ============================================================
# 2. Sharpening
# ============================================================

sharpening_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# Apply sharpening
sharpened_image = cv2.filter2D(
    image,
    -1,
    sharpening_kernel
)

# Convert BGR to RGB
sharpened_rgb = cv2.cvtColor(
    sharpened_image,
    cv2.COLOR_BGR2RGB
)

# ============================================================
# 3. Display using Matplotlib
# ============================================================

plt.figure(figsize=(15, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

# Smoothed Image
plt.subplot(1, 3, 2)
plt.imshow(smoothed_rgb)
plt.title("Gaussian Smoothed")
plt.axis("off")

# Sharpened Image
plt.subplot(1, 3, 3)
plt.imshow(sharpened_rgb)
plt.title("Sharpened Image")
plt.axis("off")

plt.tight_layout()
plt.show()
