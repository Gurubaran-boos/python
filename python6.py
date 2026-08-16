from PIL import Image, ImageEnhance

# Open the image
img = Image.open("image.jpg")

# Create brightness enhancer
enhancer = ImageEnhance.Brightness(img)

# Adjust brightness
factor = float(input("Enter brightness factor: "))

# 1.0 = Original brightness
# >1.0 = Brighter
# <1.0 = Darker
output = enhancer.enhance(factor)

# Show and save the result
output.show()
output.save("brightness_adjusted.jpg")

print("Brightness adjusted image saved as brightness_adjusted.jpg")