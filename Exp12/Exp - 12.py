import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the binary image
image = cv2.imread('/content/IMG-20251021-WA0115.jpg', 0)

# Define the structuring element for the pattern to be detected (0 for don't care, 1 for foreground, -1 for background)
pattern = np.array([[-1, 1, -1],
                    [1, 1, 1],
                    [-1, 1, -1]], dtype=np.int8)

# Apply the Hit or Miss Transformation
result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, pattern)

# Display the original image and the result
cv2_imshow(image)
cv2_imshow(result)
cv2.waitKey(0)
cv2.destroyAllWindows()