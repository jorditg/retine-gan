from __future__ import division
import torch
import math
import random
from PIL import Image, ImageOps
import numpy as np
import numbers
import types
from random import randint


class RandomVerticalFlip(object):
    """Randomly vertically flips the given PIL.Image with a probability of 0.5
    """
    def __call__(self, img):
        if random.random() < 0.5:
            return img.transpose(Image.FLIP_TOP_BOTTOM)
        return img

class RandomRotation(object):
    """Randomly rotates the given PIL.Image
    """
    def __call__(self,img):
        return img.rotate(360.*random.random())

class Random90Rotation(object):
    """Randomly rotates the given PIL.Image
    """
    def __call__(self,img):
        angle = 90.*float(randint(0,3))
        return img.rotate(angle)
                
