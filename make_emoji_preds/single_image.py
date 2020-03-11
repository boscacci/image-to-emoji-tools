#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import torch
import numpy as np
from torchvision import transforms
from torch.autograd import Variable
import torch.nn.functional as F

from utils import ConvNet
from utils import int_to_emoji_dict
from utils import NUM_CLASSES

from PIL import Image

MODEL_NAME = "make_emoji_preds/model.ckpt"

device = "cpu"
model = ConvNet(NUM_CLASSES).to(device)
model.load_state_dict(
    torch.load(MODEL_NAME, map_location=lambda storage, loc: storage)
)

imsize = 256


def make_pred(image_path):
    img = image_loader(image_path)
    model.eval()
    inputs = Variable(img).to(device)
    logits = model.forward(inputs)
    ps = F.softmax(logits, dim=1)
    topk = ps.cpu().topk(5)
    top_5_ints = topk.indices.tolist()[0]
    return [int_to_emoji_dict[x] for x in top_5_ints]


def image_loader(image_path):
    """ Scales, crops, and normalizes an image file for a PyTorch model,
        returns an Numpy array
    """
    image = Image.open(image_path).convert("RGB")
    preprocess = transforms.Compose(
        [transforms.Resize((256, 256)), transforms.ToTensor()]
    )
    image = np.expand_dims(preprocess(image), 0)
    tensor = torch.from_numpy(image)
    return tensor


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    fromfile_prefix_chars="@",
)

parser.add_argument("--filenames", "-f", help="filenames", nargs="*")
filenames = parser.parse_args().filenames

[print(filename, ": ", make_pred(filename), "\n") for filename in filenames]
