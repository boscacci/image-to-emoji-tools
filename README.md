# Instagram Relevant Emoji Tiler

Takes an image, finds semantically relevant emojis, then makes a collage/mosaic of the original image...but made out of the semantically relevant emojis!

A hacky mashup of other people's hard work:

["Emoji-Language Image Captioning with Convolutional Neural Networks" (Ian Scott Knight, Rayne Hernandez)](https://github.com/ianscottknight/Emoji-Language-Image-Captioning-with-Convolutional-Neural-Networks)

I downloaded the COCO dataset and some other (word2vec) stuff, installed Ubuntu on my hackintosh in order to run Torch in CUDA mode (to train in less than a day), and fix some typos and directory mismatch stuff in the Stanford repo in order to train and save the "model.ckpt" which drives emoji predictions. There wasn't an obvious way to make new predictions on a single image so I cobbled together a small .py script to accept one new image at a time for prediction.
 
And then:

[Nuno Faria's "Tiler"](https://github.com/nuno-faria/tiler)

Self-explanatory. I feel like the hardest part is making your new custom tiles all color balanced to RGB(240,240,240) and having the final generated tile colors come out right.

Emoji predictor selects the emoji to tile with:

🌸 🌸 🌸

<img src="images/dirkjanpiersma.jpg" width="40%"> <img src="images/flower_mosaic.png" width="40%">

🐶 🐶 🐶

<img src="images/rude.jpg" width="40%"> <img src="images/rude_mosaic.png" width="40%">

🐏, 🌄, and 🏔️

<img src="images/valley.jpg" width="40%"> <img src="images/valley_mosaic.png" width="40%">

[Follow this on instagram](https://www.instagram.com/image_to_emoji_mosaic/)