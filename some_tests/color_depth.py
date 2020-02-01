from PIL import Image

# Create an Image object from an Image
faceName = "./test.png"
imageObject = Image.open(faceName)

# gimp постеризация 12 бит -> 2^4 = 16 цветов синего красного и зеленого = 4096

# Crop the iceberg portion

# cropped     = imageObject.crop((100,30,400,300))
image_path = "test_c_d.png"
format = "PNG"

img = imageObject.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    new_item = (item[0]//16 * 16, item[1]//16 * 16, item[2]//16 * 16)
    newData.append(new_item)

img.putdata(newData)

img.save(image_path, format)
