from PIL import Image
import random


def display_image(im):
    fn = str(random.randint(1, 500)) + ".bmp"
    im.save(fn)
    print("<img src=\"/resources/{}\">".format(fn))
    # optional - comment if you don't want an additional space after the image is displayed
    print ""


Image.Image.show = display_image

# this code saves an example image as "example.jpg"
import urllib, cStringIO

# Change this URL if you want to change the image:
URL = "https://image.ibb.co/htsphz/example_color.jpg"
file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = Image.open(file)
img.save("example.jpg")