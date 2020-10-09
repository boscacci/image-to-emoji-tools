#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os

import numpy as np
from PIL import Image
import torch
from torchvision import transforms
from torch.autograd import Variable
import torch.nn.functional as F

from utils import ConvNet
from utils import int_to_emoji_dict
from utils import NUM_CLASSES

imsize = 256

MODEL_NAME = "model.ckpt"

device = "cpu"


# def get_ckpt():
#     bucket = boto3.resource("s3").Bucket("image-emoji-resources-zappa")
#     lambda_local_filepath = "/tmp/model.ckpt"
#     bucket.download_file("model.ckpt", lambda_local_filepath)
#     return lambda_local_filepath


def make_pred(image_path):
    model = ConvNet(NUM_CLASSES).to(device)
    model.load_state_dict(
        torch.load(MODEL_NAME, map_location=lambda storage, loc: storage)
    )
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
    tensor = torch.from_numpy(image)
    return tensor


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    fromfile_prefix_chars="@",
)