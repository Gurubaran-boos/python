from PIL import Image

# Open the image
img = Image.open("image.jpg")

# Convert image to grayscale
img = img.convert("L")

# Display pixel values as numbers
for y in range(img.height):
    for x in range(img.width):
        print(img.getpixel((x, y)), end=" ")
    print()