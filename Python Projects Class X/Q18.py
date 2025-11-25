from PIL import Image

# Open the image
img = Image.open("download.jpg")

# Convert to RGB if needed
img = img.convert("RGB")

# Get width and height
width, height = img.size

print("Image size:", width, "x", height)

# Accessing pixels
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        print(f"Pixel at ({x}, {y}) = R:{r}, G:{g}, B:{b}")
