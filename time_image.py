from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from time import strftime


DEFAULT_FILENAME = 'time.png'
FONT_FILE = '/usr/share/fonts/truetype/DejaVuSans.ttf'
IMAGE_FONT = ImageFont.truetype(FONT_FILE, 25)
IMAGE_TYPE = 'RGBA'
IMAGE_SIZE = (165, 40)
IMAGE_COLOR = (20, 20, 20, 0)
TIME_TEXT = strftime('%I:%M:%S %p')
TEXT_START = (0, 0)
TEXT_COLOR = (0, 0, 0)


def create_time_image(filename=DEFAULT_FILENAME):
    img = Image.new(IMAGE_TYPE, IMAGE_SIZE, IMAGE_COLOR)
    draw = ImageDraw.Draw(img)
    draw.text(TEXT_START, TIME_TEXT, TEXT_COLOR, font=IMAGE_FONT)
    ImageDraw.Draw(img)
    img.save(filename)

create_time_image()
