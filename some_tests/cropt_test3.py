from PIL import Image

# Create an Image object from an Image
faceName = "./iiWvJbw.png"
imageObject = Image.open(faceName)

# Crop the iceberg portion

# cropped     = imageObject.crop((100,30,400,300))
image_path = "./doom/%s_%s.png"
fmt = "PNG"

dx = 0  # todo to width + transparent
dy = 0

x_offset = 4 - dx
y_offset = 4 - dy
width = 52 + dx
height = 65 + dy

cols = range(6)  # 6 - 1  # cpu
rows = range(6)  # 2 - 1  # bat

diff_x = 0
diff_y = 0

for col in cols:
    for row in rows:

        x_start = x_offset + col * (diff_x + width)
        y_start = y_offset + row * (diff_y + height)

        box = (x_start, y_start, x_start + width, y_start + height)
        cropped = imageObject.crop(box)

        img = cropped.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)

        img.save(image_path % (row, col), fmt)

# Display the cropped portion

# cropped.show()
