import os
import traceback
import sys
from flask import Flask, jsonify, request
from executors.dnn_inferrer import DnnInferrer
from utils.download import download_process
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
app = Flask(__name__)

APP_ROOT = os.getenv('APP_ROOT', '/infer')
HOST = "127.0.0.1"
PORT_NUMBER = int(os.getenv('PORT_NUMBER', 5000))

u_net = DnnInferrer()


@app.route(APP_ROOT, methods=["POST"])
async def infer():
    data = request.json
    image = data['image']
    model = data['model']

    dirs = os.listdir("weights/")
    key = 0

    for dir in dirs:
        if dir == "bvlc_googlenet.caffemodel":
            key += 1
    if key == 0:
        c = download_process("GoogleNet", "weights/")
        await c.process()
        return {'segmentation_output': "dosya yuklemesi yapıldı"}


    result = u_net.infer(image)


    return result


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(stackTrace=traceback.format_exc())


if __name__ == '__main__':
    app.run(host=HOST, port=PORT_NUMBER)
