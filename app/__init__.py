from flask import Flask
from app.ext import init_ext
from app import settings

def create_app(env):
    app =Flask(__name__)
    app.config.from_object(settings.config.get(env,"default"))
    init_ext(app)
    return app


