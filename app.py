from flask import Flask
import os


class Config:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
    DEBUG = True


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)