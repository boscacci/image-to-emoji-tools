#!/bin/bash

# You will need to save $insta_user and $insta_pass as bash variables
# Probably best accomplished by exporting in .bash_profile or .bashrc

python instagram_scraper/app.py \
-f instagram_scraper/ig_users.txt \
-u $insta_user \
-p $insta_pass \
--maximum 15 \
--media-types image \
--destination scraped_images/ \
--retain-username \
--template '{username}_{year}-{month}-{day}'