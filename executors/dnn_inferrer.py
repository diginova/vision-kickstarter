import cv2
import numpy as np
import sys
import os
import json
from PIL import Image as im

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from utils.config import Config
from configs.config import CFG


class DnnInferrer:
    def __init__(self):
        self.config = Config.from_json(CFG)
        self.image_size = self.config.data.image_size

        self.model = None
        self.predict = None

    def MobilNetSSD(self, image):

        image_new = image
        self.model = cv2.dnn.readNetFromCaffe('weights/mobilenet_ssd/MobileNetSSD_deploy.prototxt.txt',
                                              'weights/mobilenet_ssd/MobileNetSSD_deploy.caffemodel')

        dim = (300, 300)
        image_new = cv2.resize(image_new, dim, interpolation=cv2.INTER_AREA)

        blob = cv2.dnn.blobFromImage(image_new, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)

        with open('weights/mobilenet_ssd/classes.txt') as f:
            lines = f.readlines()
        f.close()
        class_names = lines[0].split()

        # set the blob to the model
        self.model.setInput(blob)
        # forward pass through the model to carry out the detection
        output = self.model.forward()
        # loop over each of the detection
        result = []
        for detection in output[0, 0, :, :]:
            # extract the confidence of the detection
            confidence = detection[2]
            # draw bounding boxes only if the detection confidence is above...
            # ... a certain threshold, else skip
            veri = {
                "class": "",
                "confidence": "",
                "x": "",
                "y": "",
                "width": "",
                "height": "",
            }
            if confidence > 0.4:
                confidence = np.float64(confidence)
                veri.update({"confidence": confidence})
                # get the class id
                class_id = detection[1]
                # map the class id to the class
                class_name = class_names[int(class_id) - 1]
                veri.update({"class": class_name})
                # get the bounding box coordinates
                box_x = detection[3] * 300
                box_y = detection[4] * 300
                veri.update({"x": int(box_x)})
                veri.update({"y": int(box_y)})
                # get the bounding box width and height
                box_width = detection[5] * 300
                box_height = detection[6] * 300
                veri.update({"width": int(box_width)})
                veri.update({"height": int(box_height)})
                result.append(veri)
        sonuc = json.dumps(result)

        return sonuc

    def infer(self, image):
        data = np.asarray(image, dtype=np.float32)
        result = self.MobilNetSSD(data)

        return {'segmentation_output': result}