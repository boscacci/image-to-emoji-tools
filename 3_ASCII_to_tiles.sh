#!/bin/bash

python make_mosaics/emoji_to_gray_jpg.py $1 
NEWEST_TILE="$(ls -Art make_mosaics/tiles/ | tail -n 1)"
python make_mosaics/gen_tiles.py make_mosaics/tiles/$NEWEST_TILE
