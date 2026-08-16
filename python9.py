import cv2

# Read the image
img = cv2.imread("image.jpg")

# Apply averaging filter
result = cv2.blur(img, (3, 3))

# Display the image
cv2.imshow("Original Image", img)
cv2.imshow("Averaging Filter", result)

# Wait for a key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()