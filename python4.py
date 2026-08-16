from PIL import Image

# Open the image
img = Image.open("image.jpg")

# Rotate the image by 90 degrees
rotated_img = img.rotate(90)

# Save the rotated image
rotated_img.save("rotated_image.jpg")

# Display the image
rotated_img.show()