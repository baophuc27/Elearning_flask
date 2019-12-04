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
       User.query.getListFName(db)
       return render_template("index.html")
    
    @app.route("/truclu")
    def truc():
        print("asdfad")
        return render_template("index.html")

    return app


