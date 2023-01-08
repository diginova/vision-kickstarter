import os
import traceback
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from flask import Flask, jsonify, request
from src.executor.unet_inferrer import  UnetInferrer
app = Flask(__name__)

APP_ROOT = os.getenv('APP_ROOT', '/api')
HOST = "0.0.0.0"
PORT_NUMBER = int(os.getenv('PORT_NUMBER', 5000))

u_net = UnetInferrer()


@app.route(APP_ROOT, methods=["POST"])
def api():
    data = request.json
    image = data['image']
    return u_net.infer(image)


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(stackTrace=traceback.format_exc())


if __name__ == '__main__':
    app.run(host=HOST, port=PORT_NUMBER)


