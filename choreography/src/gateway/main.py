import os, gridfs, pika, json
from flask import Flask, request, send_file
# import PyMongo

from bson.objectid import ObjectId

from auth_service.service import AuthService

server = Flask(__name__)


# mongo_video = PyMongo(server, uri="mongodb://host.minikube.internal:27017/videos")
#
# mongo_mp3 = PyMongo(server, uri="mongodb://host.minikube.internal:27017/mp3s")

# fs_videos = gridfs.GridFS(mongo_video.db)
# fs_mp3s = gridfs.GridFS(mongo_mp3.db)

# credentials = pika.PlainCredentials('guest', 'guest')
# parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
# connection = pika.BlockingConnection(parameters)
# channel = connection.channel()
# channel.queue_declare(queue='hello')
#
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello W0rld!')
# print(" [x] Sent 'Hello World!'")
# connection.close()


@server.route("/login", methods=["POST"])
def login():
    auth_service = AuthService(request)
    token, err = auth_service.login()

    if not err:
        return token
    else:
        return err


@server.route('/register', methods=["POST"])
def register():
    auth_service = AuthService(request)
    token, err = auth_service.register()
    if not err:
        return token
    else:
        return err


@server.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]


@server.route("/download", methods=["GET"])
def download():
    file = request.files["file"]


if __name__ == "__main__":
    server.run()
