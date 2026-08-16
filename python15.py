import cv2

# Read the image
img = cv2.imread("image.jpg")

# Scale the image to 2 times its original size
scaled = cv2.resize(img, None, fx=2, fy=2)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Scaled Image", scaled)

# Wait for a key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()