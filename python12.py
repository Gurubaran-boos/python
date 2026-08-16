import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

# Create a 3x3 kernel
kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
], dtype=np.float32) / 9

# Apply the kernel using filter2D()
result = cv2.filter2D(img, -1, kernel)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", result)

# Wait for a key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()