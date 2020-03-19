# Takes: emoji ASCII character
# Returns: large gray jpg version (RGB 240,240,240)

import sys
import os
import pickle

from bs4 import BeautifulSoup as bs
from PIL import Image, ImageOps
from io import BytesIO
from base64 import b64decode


def make_unicode(ascii_emoji):
    uni_emoji = ascii_emoji.encode("unicode-escape").decode()
    uni_emoji = uni_emoji.strip("\\").upper()
    unic = uni_emoji.split("\\")[0]
    return unic


def make_png(unicode_str):
    with open("make_mosaics/emojidict.pickle", "rb") as pickle_file:
        emoji_webpage = pickle.load(pickle_file).text
    soup = bs(emoji_webpage, "html.parser")

    for tr in soup.select("tr"):
        try:
            row_unicode = tr.findAll("td")[1].a.text.split("+")[1]
        except IndexError:
            continue
        if row_unicode in unicode_str:
            image_uri = tr.findAll("td")[2].img["src"].split("64,")[1]
            break

    im = Image.open(BytesIO(b64decode(image_uri)))
    return im.convert("RGBA")


def tint_image(src, color=(240, 240, 240)):
    src.load()
    r, g, b, alpha = src.split()
    gray = ImageOps.grayscale(src)
    result = ImageOps.colorize(gray, (230, 230, 230, 0), color)
    result.putalpha(alpha)
    return result


ascii_emoji = sys.argv[1]
unic = make_unicode(ascii_emoji)
im = make_png(unic)
tinted = tint_image(im)
# tinted.show()
tinted.save(f"make_mosaics/tiles/{unic}.png")
