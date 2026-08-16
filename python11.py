import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

# Define sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply the kernel
sharpened = cv2.filter2D(img, -1, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

# Wait for key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()