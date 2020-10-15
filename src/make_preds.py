#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import pickle

import numpy as np
from PIL import Image

from torchvision import transforms

from torch.autograd import Variable
from torch import from_numpy
import torch.nn.functional as F

# from utils import ConvNet
from utils import int_to_emoji_dict
from utils import NUM_CLASSES

imsize = 256

MODEL_NAME = "model.ckpt"

device = "cpu"


def make_pred(image_path):
    filehandler = open("trained_emoji_model.obj", "rb")
    model = pickle.load(filehandler)
    filehandler.close()
    ###
    img = image_loader(image_path)
    model.eval()
    inputs = Variable(img).to(device)
    logits = model.forward(inputs)
    ps = F.softmax(logits, dim=1)
    topk = ps.cpu().topk(5)
    top_5_ints = topk.indices.tolist()[0]
    return [int_to_emoji_dict[x] for x in top_5_ints]


def image_loader(image_path):
    """Scales, crops, and normalizes an image file for a PyTorch model,
    returns an Numpy array
    """
    image = Image.open(image_path).convert("RGB")
    preprocess = transforms.Compose(
        [transforms.Resize((256, 256)), transforms.ToTensor()]
    )
    image = np.expand_dims(preprocess(image), 0)
    tensor = from_numpy(image)
    return tensor


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    fromfile_prefix_chars="@",
)