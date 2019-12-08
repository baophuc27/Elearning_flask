from flask import *
from flask_sqlalchemy import SQLAlchemy
from .models import User
from .models import Course
from config import app_config
import hashlib

def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db=SQLAlchemy(app)
    db.init_app(app)
    app.secret_key = "super secret key"


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
                flash("Login successful!")
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

            User.query.createnewuser(db,name,gender,birthday,address,password,displayname,role)
            return render_template("home.html")

    #--------------BAO PHUC--------------------
    @app.route("/dicussion")
    def dicussion():
        return render_template("dicussion.html")
    #-------------HET BAO PHUC-----------------
   
    #-------------------------------------------------------------------------------------------------
    @app.route("/main")
    def mainpage():
        return render_template("main.html")
    
    @app.route("/course")
    
    def course():
        lst = Course.Query.getdataCourse(db)
        raw = json.dumps(lst)
        data = json.loads(raw)
        return render_template("course.html", data = data)
    
    
    @app.route("/lesson")
    def lesson():
        courseId = request.args.get('data-id')
        print(courseId)
        lst = Course.Query.getdataLesson(db,courseId)
        raw = json.dumps(lst)
        data = json.loads(raw)
        return render_template("lesson.html", data = data)
    
    @app.route("/curriculum")
    def curriculum():
        lst = Course.Query.getdataCurriculum(db)
        raw = json.dumps(lst)
        data = json.loads(raw)
        return render_template("curriculum.html", data = data)
    
    @app.route("/topic")
    def topic():
        lst = Course.Query.getdataTopic(db)
        raw = json.dumps(lst)
        data = json.loads(raw)
        return render_template("topic.html", data = data)

   
    @app.route("/searchCourseOfCurri")

    def searchCourseofCurri():
        namecourse = request.args.get('searchCurri')
        lst = Course.Query.searchCurriculum(db,namecourse)
        print(lst)
        raw = json.dumps(lst)
        data = json.loads(raw)
        fee_curriculum = Course.Query.calculateCurriculum(db,namecourse)
        return render_template("searchCourseOfCurri.html", data = data,  fee_curriculum = fee_curriculum)
    
    @app.route("/searchCourseOfTopic")

    def searchCourseofTopic():
        nametopic = request.args.get('searchTopic')
        lst = Course.Query.searchTopic(db,nametopic)
        raw = json.dumps(lst)
        data = json.loads(raw)
        return render_template("searchCourseOfTopic.html", data = data)
    
    @app.route("/searchCondition")
    def search():
        name = request.args.get('searchNum')
        lst = Course.Query.search(db,name)
        raw = json.dumps(lst)
        data = json.loads(raw)
        return render_template("searchCondition.html", data = data)

    return app

