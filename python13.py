import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

# Get image dimensions
rows, cols = img.shape[:2]

# Create translation matrix
# Move 100 pixels right and 50 pixels down
M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

# Apply translation
translated = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)

# Wait for key
cv2.waitKey(0)
cv2.destroyAllWindows()