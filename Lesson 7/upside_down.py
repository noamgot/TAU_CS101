from PIL import Image
import IP

img = Image.open("example.jpg")
img = img.convert('L')


def upside_down(im):
    w, h = im.size
    im_new = Image.new('L', (w, h), 255)
    mat = im.load()
    mat_new = im_new.load()
    for x in range(w):
        for y in range(h):
            mat_new[x, y] = mat[x, h - y - 1]

    return im_new


img.show()
img2 = upside_down(img)
img2.show()