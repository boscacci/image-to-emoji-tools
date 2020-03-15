#!/bin/bash

python instagram_scraper/app.py \
-f instagram_scraper/ig_users.txt \
-u $insta_user \
-p $insta_pass \
-m 15 \
-t image \
-d scraped_images/ \
-n
