from PIL import Image
import numpy as np

# Open the image
img = Image.open("image.jpg").convert("L")

# Convert image to array
pixels = np.array(img)

# Set threshold value
threshold = 128

# Apply thresholding
output = np.where(pixels > threshold, 255, 0).astype(np.uint8)

# Convert array back to image
result = Image.fromarray(output)

# Display the image
result.show()

# Save the image
result.save("threshold_image.jpg")

print("Thresholding completed successfully!")