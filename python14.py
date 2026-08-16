from PIL import Image
import numpy as np

# Read the image
img = Image.open("image.jpg").convert("L")

# Convert image to array
pixels = np.array(img)

# Point-to-point transformation
# Invert the pixel values
output = 255 - pixels

# Convert back to image
result = Image.fromarray(output)

# Display the image
result.show()

# Save the result
result.save("point_to_point.jpg")

print("Point-to-point transformation completed!")