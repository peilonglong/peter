#!/usr/bin/python
# -*- coding:<encoding utf8> -*-
from app import create_app
# from app.admin.functions import create_app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app.ext import db
# from app.models import *
app = create_app("develop")
manager = Manager(app)
#1.绑定app,和db
#2.Migrate_command 命令添加到manage中
migrate = Migrate(app,db) # 实例化迁移对象

manager.add_command("db",MigrateCommand) # 添加迁移命令
debug=True
if __name__=="__main__":
    manager.run()