from flask import Flask
# from flask_migrate.templates.flask import env

from app.admin.views import blue
from app.ext import init_ext
#函数创建app 并注册app 最后return
def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    return app