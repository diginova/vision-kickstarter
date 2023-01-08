import requests
from PIL import Image
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from src.config.config import CFG
from src.util.config import Config
ENDPOINT_URL = "http://127.0.0.1:5000/api"

def inference():
    config = Config.from_json(CFG)
    image = np.asarray(Image.open(config.project.path + '/resources/yorkshire_terrier.jpg')).astype(np.float32)
    data ={'image': image.tolist()}
    response = requests.post(ENDPOINT_URL, json = data)
    print(response.raise_for_status())
    print(response.json())


if __name__ =="__main__":
    inference()
