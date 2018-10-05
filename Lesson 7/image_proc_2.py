from PIL import Image
import IP

img = Image.open("example.jpg")
img = img.convert('L')
#img.show()

slice = img.crop((30,20,80,80))
#slice.show()
img2 = img.rotate(-90)
#img2.show()
hist = img.histogram()
print(hist)