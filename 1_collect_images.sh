#!/bin/bash

python instagram_scraper/app.py \
-f instagram_scraper/ig_users.txt \
-u $insta_user \
-p $insta_pass \
--maximum 15 \
--media-types image \
--destination scraped_images/ \
--template '{username}_{year}-{month}-{day}'