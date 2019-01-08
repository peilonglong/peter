#encoding:utf8
import os
from flask import Blueprint
from flask import render_template, redirect, request, url_for, flash
import uuid
from app.ext import db
from .forms import LoginForm
from app.models import UserModel
from flask_login import login_user, logout_user, login_required
#视图函数中调用blue 并浏览器访问它 实例化一个blue


blue = Blueprint("blue",__name__)


@blue.route("/index")
def index():
    return render_template("admin/index.html")

@blue.route("/login",methods=['GET', 'POST'])
def login():
    #用户登录，
    #判断是否为post/get
    #post 在数据库中判断用户名或者密码，登录成功 进入首页
    #！post提交时，返回重新登录
    data={}
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        #在数据库中查询比较
        user= UserModel.query.filter_by(username=username,password=password)
        if user.count() > 0:#判断用户的个数
            user=user.first() #获取第一个
            data["username"]=user.username
            data["password"]=user.password
        return render_template('admin/index.html',data=data)
    else:
        flash('用户名或密码错误')
    return redirect(url_for("blue.login"))

#退出
@blue.route('/logout')
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('blue.login'))




