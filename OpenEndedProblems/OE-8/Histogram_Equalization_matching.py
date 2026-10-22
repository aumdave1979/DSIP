import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms
import os

def process_and_display_image(image_path, reference_image_path=None, image_label="Image 1"):
    """
    Reads an image, applies Histogram Equalization and Histogram Matching,
    prints the mean and std deviation, and plots the results.
    """
    # 1. Load the original image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # 2. Histogram Equalization
    img_eq = cv2.equalizeHist(img)

    # 3. Histogram Matching
    # Histogram matching requires a reference image to match the distribution against.
    # If no reference is provided, this falls back to matching against a uniform gradient 
    # just so the code executes, but you should provide a real reference image.
    if reference_image_path and os.path.exists(reference_image_path):
        ref_img = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)
        img_matched = match_histograms(img, ref_img).astype('uint8')
    else:
        # Dummy reference (creates a uniform distribution) if none is provided
        ref_img = np.linspace(0, 255, img.size).reshape(img.shape).astype('uint8')
        img_matched = match_histograms(img, ref_img).astype('uint8')

    # --- Terminal Output Formatting ---
    print(image_label)
    print(f"Original     : mean = {np.mean(img):.1f}   std = {np.std(img):.1f}")
    print(f"Equalization : mean = {np.mean(img_eq):.1f}   std = {np.std(img_eq):.1f}")
    print(f"Matching     : mean = {np.mean(img_matched):.1f}   std = {np.std(img_matched):.1f}")

    # --- Plotting ---
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    fig.canvas.manager.set_window_title(f'Output in images (comparison) - {image_label}')

    # Top Row: Images
    axes[0, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[0, 0].set_title('Original', fontsize=10)
    axes[0, 0].axis('off')

    axes[0, 1].imshow(img_eq, cmap='gray', vmin=0, vmax=255)
    axes[0, 1].set_title('Histogram Equalization', fontsize=10)
    axes[0, 1].axis('off')

    axes[0, 2].imshow(img_matched, cmap='gray', vmin=0, vmax=255)
    axes[0, 2].set_title('Histogram Matching', fontsize=10)
    axes[0, 2].axis('off')

    # Bottom Row: Histograms
    # Original Histogram (Gray)
    axes[1, 0].hist(img.ravel(), bins=256, range=[0, 256], color='gray')
    axes[1, 0].set_title('Histogram - Original', fontsize=10)
    axes[1, 0].set_xlabel('Gray level (0-255)', fontsize=8)
    axes[1, 0].set_ylabel('Number of pixels', fontsize=8)
    axes[1, 0].grid(alpha=0.3)

    # Equalization Histogram (Blue)
    axes[1, 1].hist(img_eq.ravel(), bins=256, range=[0, 256], color='blue')
    axes[1, 1].set_title('Histogram - Equalization', fontsize=10)
    axes[1, 1].set_xlabel('Gray level (0-255)', fontsize=8)
    axes[1, 1].set_ylabel('Number of pixels', fontsize=8)
    axes[1, 1].grid(alpha=0.3)

    # Matching Histogram (Green)
    axes[1, 2].hist(img_matched.ravel(), bins=256, range=[0, 256], color='green')
    axes[1, 2].set_title('Histogram - Matching', fontsize=10)
    axes[1, 2].set_xlabel('Gray level (0-255)', fontsize=8)
    axes[1, 2].set_ylabel('Number of pixels', fontsize=8)
    axes[1, 2].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()

# ==========================================
# Execution Example
# ==========================================
if __name__ == "__main__":
    # Replace these paths with the actual locations of your images
    target_image = '/content/aquarium.jpg'
    reference_image = '/content/sunset.jpg' 
    
    process_and_display_image(target_image, reference_image, image_label="Image 1")
    print("Done")