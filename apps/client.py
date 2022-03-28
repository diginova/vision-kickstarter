import requests
from PIL import Image
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

ENDPOINT_URL = "http://127.0.0.1:5000/infer"


def infer():
    image = np.asarray(Image.open('resources/street.jpg')).astype(np.float32)
    data = {'image': image.tolist(), 'model': "GoogleNet"}
    response = requests.post(ENDPOINT_URL, json=data)
    print(response.raise_for_status())
    print(response.json())


if __name__ == "__main__":
    infer()