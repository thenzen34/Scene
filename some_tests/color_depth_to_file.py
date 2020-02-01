from PIL import Image

# Create an Image object from an Image
faceName = "./doom/0_0.png"
imageObject = Image.open(faceName)

# gimp постеризация 12 бит -> 2^4 = 16 цветов синего красного и зеленого = 4096

img = imageObject.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    newData.append("0x" + format(item[0] // 16, "1x") + format(item[1] // 16, "1x") + format(item[2] // 16, "1x"))

# SA60LCD
print(len(newData), ", ".join(newData))
