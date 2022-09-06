from PIL import Image, ImageDraw, ImageFont
from deepMazeRL.params import SPRITE_SIZE

def cropear(input_image, height, width):
    im = Image.open(input_image)
    imgwidth, imgheight = im.size
    images = []
    
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            a = a.resize((SPRITE_SIZE, SPRITE_SIZE), Image.ANTIALIAS)
            images.append(a)
            # a.show()
    return images

def colors_for_values(values):
    colors = [(255, 255, 255) for _ in range(4)]
    colors[np.argmax(values)] = (0, 255, 0)
    colors[np.argmin(values)] = (255, 0, 0)
    return colors