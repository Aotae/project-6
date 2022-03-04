"""
Brevets RESTful API
"""
from flask import Flask
import os
from flask_restful import Api
from mongoengine import connect
from resources import BrevetsAPI,BrevetAPI

API_PORT  = os.environ.get('API_PORT')

app = Flask(__name__)
myapi= Api(app)
connect(host="mongodb://db:27017/brevets")

myapi.add_resource(BrevetAPI,"/api/brevet/<id>")
myapi.add_resource(BrevetsAPI,"/api/brevets")

if __name__ == "__main__":
    print("OPEN ON API", API_PORT)
    print("Opening api for global access on port {}".format(API_PORT))
    app.run(port=API_PORT, host="0.0.0.0")
