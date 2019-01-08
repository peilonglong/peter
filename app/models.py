#encoding:utf-8
from datetime import datetime
from app.ext import db


#用户表
class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.String(64),nullable=False)
    role = db.Column(db.String(64), nullable=True)  #角色
    password = db.Column(db.String(128))        #密码
    start = db.Column(db.String(30),nullable=False)
    create_time  = db.Column(db.DateTime, nullable=True,default=datetime.now)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username


#角色表
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')  #反向引用查询管联，一对一时 uselist=False

    def __repr__(self):
        return '<Role %r>' % self.name
