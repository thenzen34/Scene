from PIL import Image

# Create an Image object from an Image
faceName = "./d7q0roz-defec22c-41e1-4715-bae7-28ba90ab8684.png"
imageObject = Image.open(faceName)

# Crop the iceberg portion

# cropped     = imageObject.crop((100,30,400,300))
image_path = "./1.png"
fmt = "PNG"
x_offset = 14
y_offset = 14 + 1
width = 71
height = 92

col = 2
row = 5

diff_x = 9
diff_y = 9

x_start = x_offset + (col - 1) * (diff_x + width + 1)
y_start = y_offset + (row - 1) * (diff_y + height + 1)

box = (x_start - 1, y_start - 1, x_start + width + 1, y_start + height + 1)
cropped = imageObject.crop(box)
cropped.save(image_path, fmt)

# Display the cropped portion

# cropped.show()
