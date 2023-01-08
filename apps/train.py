# -*- coding: utf-8 -*-
""" train.py """
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from src.configs.config import CFG
from src.models.unet import UNet


def train():
    """Builds model, loads data, trains and evaluates"""
    model = UNet(CFG)
    model.load_data()
    model.build()
    model.train()
    model.evaluate()


if __name__ == '__main__':
    train()
