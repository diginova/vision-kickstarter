import cv2
import numpy as np
import argparse

'''
#MobilNetSSD
path_classes = '/opt/project/weights/mobilenet_ssd/classes.txt'
path_prototxt = '/opt/project/weights/mobilenet_ssd/MobileNetSSD_deploy.prototxt.txt'
path_caffemodel = '/opt/project/weights/mobilenet_ssd/MobileNetSSD_deploy.caffemodel'
'''

# alexnet
# path_classes = '/opt/project/weights/alexnet/classes.txt'
path_prototxt = '/opt/project/weights/alexnet/deploy.prototxt.txt'
path_caffemodel = '/opt/project/weights/alexnet/bvlc_alexnet.caffemodel'
'''

#googlenet
path_prototxt = '/opt/project/weights/googlenet/solver.prototxt.txt'
path_caffemodel = '/opt/project/weights/googlenet/bvlc_googlenet.caffemodel'
'''

# List of categories and classes
categories = {0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird',
              4: 'boat', 5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat',
              9: 'chair', 10: 'cow', 11: 'diningtable', 12: 'dog',
              13: 'horse', 14: 'motorbike', 15: 'person',
              16: 'pottedplant', 17: 'sheep', 18: 'sofa',
              19: 'train', 20: 'tvmonitor'}

'''
with open(path_classes) as f:
    lines = f.readlines()
f.close()
class_names = lines[0].split()
'''
# get a different color array for each of the classes
COLORS = np.random.uniform(0, 255, size=(20, 3))

# Load the pre-trained neural network
model = cv2.dnn.readNetFromCaffe(path_prototxt, path_caffemodel)

# read the image from disk
image = cv2.imread('resources/bycle.jpg')
# image_height, image_width, _ = image.shape
print(type(image))
dim = (300, 300)
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
image_height, image_width, _ = image.shape

# create blob from image
# blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), swapRB=True)

print(type(image))
blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)

COLORS = np.random.uniform(0, 255, size=(20, 3))

# set the blob to the model
model.setInput(blob)
# forward pass through the model to carry out the detection
output = model.forward()
# loop over each of the detection

result = []
for detection in output[0, 0, :, :]:
    # extract the confidence of the detection
    confidence = detection[2]
    # draw bounding boxes only if the detection confidence is above...
    # ... a certain threshold, else skip
    veri = {
        "class": "",
        "confidence": 0,
        "x": 0,
        "y": 0,
        "width": 0,
        "height": 0,
    }
    if confidence > .4:
        confidence = np.float64(confidence)
        veri.update({"confidence": confidence})
        # get the class id
        class_id = detection[1]
        # map the class id to the class
        # class_name = class_names[int(class_id) - 1]
        # veri.update({"class": class_name})
        # get the bounding box coordinates
        box_x = detection[3] * 300
        box_y = detection[4] * 300
        veri.update({"x": box_x})
        veri.update({"y": box_y})
        # get the bounding box width and height
        box_width = detection[5] * 300
        box_height = detection[6] * 300
        veri.update({"width": box_width})
        veri.update({"height": box_height})
        result.append(veri)
        color = COLORS[int(class_id)]

        cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=1)

        # put the FPS text on top of the frame

        cv2.putText(image, confidence, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1)

cv2.imwrite('image_bycle_result.jpg', image)

cv2.waitKey(0)

cv2.destroyAllWindows()

for veri in result:
    print(veri)