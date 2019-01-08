#coding:utf8
from flask import Flask
import os
from app.admin import blue as admin_blueprint

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR,'static')
    templates_dir = os.path.join(BASE_DIR,'templates')

    app = Flask(__name__,static_folder=static_dir,template_folder=templates_dir)
    app.register_blueprint(admin_blueprint,url_prefix="/admin")
    return app