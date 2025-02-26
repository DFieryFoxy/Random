import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "bi_ro.gif", save_all=True, append_images=[images[2]], duration=300, loop=0
)