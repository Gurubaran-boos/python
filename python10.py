import cv2

# Read the image
img = cv2.imread("image.jpg")

# Apply Gaussian filter
result = cv2.GaussianBlur(img, (5, 5), 0)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Filter", result)

# Wait for a key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()