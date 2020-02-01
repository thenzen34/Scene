from PIL import Image

# Create an Image object from an Image
faceName = "./iiWvJbw.png"
imageObject = Image.open(faceName)

# Crop the iceberg portion

# cropped     = imageObject.crop((100,30,400,300))
image_path = "./2.png"
fmt = "PNG"

dx = 2  # todo to width + transparent
dy = 1

x_offset = 4 - dx
y_offset = 4 - dy
width = 48 + dx + 1
height = 60 + dy + 1

col = 7
row = 1

diff_x = 3 - dx
diff_y = 5 - dy

x_start = x_offset + (col - 1) * (diff_x + width)
y_start = y_offset + (row - 1) * (diff_y + height)

box = (x_start, y_start, x_start + width, y_start + height)
cropped = imageObject.crop(box)
cropped.save(image_path, fmt)

# Display the cropped portion

# cropped.show()
