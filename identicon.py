import customidenticon
import hashlib
from PIL import Image, ImageOps


identicon = customidenticon.create(
    "8cf8a9d0252fe36bf98aaf70be95b679f1eebf4709d0ef0E32b4f8236b152f14",            # Data
    type="pixels",          # Type of algorithm (pixels, blocks or layers)
    format="png",           # Output format
    salt="Aziiz was here",                # salt for more variants
    background="white",   # background color
    block_visibility=150,   # transparency of elements in the image (0-255)
    block_size=100,          # size of elements (px)
    border=0,              # border (px)
    size=10,                # number of elements
    hash_func= hashlib.sha3_256          # hash function (auto)
)


#identicon = customidenticon.create("T2est data", hash_func=hashlib.sha3_256)


with open("identicon/identicon.png", "wb") as f:
    f.write(identicon)

ImageOps.expand(Image.open('identicon/identicon.png'),border=50,fill='#404040').save('imaged-with-border.png')
