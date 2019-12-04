from flask import *
from flask_sqlalchemy import SQLAlchemy
from .models import User
from config import app_config


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
            if User.query.getNameandPass(db,name,password):
                return render_template("home.html")
            

    return app


