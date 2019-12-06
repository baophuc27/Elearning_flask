from flask import *
from flask_sqlalchemy import SQLAlchemy
from .models import User
from config import app_config
import hashlib

def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db=SQLAlchemy(app)
    db.init_app(app)

    @app.route("/")
    def index():
       return render_template("index.html")
    
    @app.route("/login",methods=["POST"])
    def login():
        if request.method=="POST":
            name = request.form['name']
            password = request.form['password']
            password=hashlib.md5(password.encode("utf-8")).hexdigest()
            if User.query.getNameandPass(db,name,password):
                session['username']=name
                return render_template("home.html")
            
    #--------------BAO PHUC--------------------
    @app.route("/dicussion")
    def dicussion():
        return render_template("dicussion.html")

    #-------------HET BAO PHUC-----------------
    return app


