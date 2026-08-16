from PIL import Image, ImageEnhance

# Open the image
img = Image.open("image.jpg")

# Create brightness enhancer
enhancer = ImageEnhance.Brightness(img)

# Change brightness
# 1.0 = original
# > 1.0 = brighter
# < 1.0 = darker
bright_img = enhancer.enhance(1.5)

# Save the new image
bright_img.save("bright_image.jpg")

# Display the image
bright_img.show()