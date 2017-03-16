from flask import Flask
from os import environ

app = Flask(__name__)
app.config.from_object('app.config')

from app import views
