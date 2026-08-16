from PIL import Image, ImageFilter

# Open the image
img = Image.open("image.jpg")

# Apply blur
blurred_img = img.filter(ImageFilter.BLUR)

# Save the blurred image
blurred_img.save("blurred_image.jpg")

# Display the image
blurred_img.show()