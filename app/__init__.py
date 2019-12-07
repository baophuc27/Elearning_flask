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
    app.secret_key = "super secret key"
    session = []

    @app.route("/")
    def index():
       return render_template("index.html")
    
    @app.route("/login",methods=["POST"])
    def login():
        if request.method=="POST":
            name = request.form['name']
            password = request.form['password']
            if name=='' or password=='':
                flash("Must be fill out username and password!")
                return render_template("index.html")
            password=hashlib.md5(password.encode("utf-8")).hexdigest()
            if User.query.getNameandPass(db,name,password):
                information = User.query.addsession(db,name)
                tmpuser= User.Users(information[0],information[1],information[2],information[3],information[6])
                session.append(tmpuser)
                return render_template("home.html")
            else:
                flash("Wrong username or password")
                return render_template("index.html")

    @app.route("/registertransfer")
    def transferregister():
        return render_template("register.html")

    @app.route("/register",methods=["POST"])
    def register():
        if request.method=="POST":
            name = request.form['name']
            password = request.form['password']
            if name=='' or password=='':
                flash("Must be fill out username and password!")
                return render_template("register.html")
            password=hashlib.md5(password.encode("utf-8")).hexdigest()
            ###check if username had been registed
            if User.query.checkifnameregisted(db,name):
                flash("User had been registed. Please choose another name!")
                return render_template("register.html")
            gender = request.form['gender']
            if (gender =='male'):
                gender='M'
            else: 
                gender='F'
            birthday= request.form['myDate']
            address= request.form['address']
            displayname = request.form['displayname']
            if displayname=='':
                flash("Must be fill out name to display")
                return render_template("register.html")
            role = request.form['role']
            ##insert into database
            phones = request.form['phone'] 
            phones = phones.split(',')
            #add phone vào
            if ( not User.query.createnewuser(db,name,gender,birthday,address,password,displayname,role)):
                flash("Teacher must be over 18 years old")
                return render_template("register.html")
            if phones!=['']:
                if (not User.query.addphone(db,name,phones)):
                    flash("Phones less than 9 digits")
                    return render_template("register.html")
            return render_template("home.html")

    @app.route("/studentlist")
    def transferstudentlist():
        return render_template("studentlist.html")

    @app.route("/teacherlist")
    def transferteacherlist():
        return render_template("teacherlist.html")


    @app.route("/searchteacher",methods=["POST"])
    def searchteacher():
        name = request.form['name']
        order = request.form['order']
        range = request.form['range']
        if name=='' or range=='':
            flash("Please fill out name and range to search!")
            return render_template('teacherlist.html')
        result = User.query.searchteacher(db,name,order,range)
        return render_template('teacherlist.html',data=result)

    return app


