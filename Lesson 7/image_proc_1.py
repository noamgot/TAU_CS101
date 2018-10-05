from PIL import Image
import IP

img = Image.open("example.jpg")
#img.show()
#print(img.size)
img2 = img.resize((100,100))
#img2.show()
img3 = img.convert('L')
#img3.show()
mat = img3.load()
#print(mat[10,20])
mat[10,20] = 255
#print(mat[10,20])
# for x in range(50):
#     for y in range(50):
#         mat[x,y] = 255
# img3.show()

# for x in range(50):
#     for y in range(50):
#         mat[x,y] = 300
# img3.show()

img4 = Image.new('L', (100,50), 128)
img4.show()