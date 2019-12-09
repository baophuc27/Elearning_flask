from flask import *
from flask_sqlalchemy import SQLAlchemy
from .models import User,Examination
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
                session['username']=name
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
    @app.route("/course")
    def course():
        return render_template("course.html")

    #--------------BAO PHUC--------------------
    @app.route("/dicussion")
    def dicussion():
        print(session['username'])
        return render_template("dicussion.html")
    #-------------HET BAO PHUC-----------------
    @app.route("/examination")
    def examination():
        courseID=request.args.get('courseID')
        return render_template("examination.html",course=courseID)
    @app.route("/fetchExam")
    def fetchExam():
        courseID=request.args.get('courseID')
        result=Examination.query.getAllExam(db,courseID)
        listExam = [[x[0],x[1],x[2]] for x in result]
        data = {
            'name':'Examination',
            'listExam': listExam
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response

    @app.route("/insertExam",methods=['POST'])
    def insertExam():
        courseID=request.form['courseID']
        examID=request.form['examID']
        print(courseID,examID)
        result=Examination.query.createExam(db,courseID,examID)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response

    @app.route("/examDelete")
    def examDelete():
        examid=request.args.get('id')
        result=Examination.query.deteleExam(db,examid)
        print(result)
        data = {
            'name':'Examination',
            'action': 'detete success'
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    @app.route("/examDetail")
    def examDetail():
        examid=request.args.get('id')
        return render_template("examdetail.html",exam=examid)
    @app.route("/fetchQuestion")
    def fetchQuestion():
        examid=request.args.get('examID')
        result=Examination.query.getAllQuestion(db,examid)
        listExam = [[x[0],x[1],x[2],x[3]] for x in result]
        data = {
            'name':'Examination',
            'listExam': listExam
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    @app.route("/insertQuestion",methods=['POST'])
    def insertQuestion():
        examID=request.form['examID']
        content=request.form['content']
        mark=request.form['mark']
        qid=request.form['qid']
        result=Examination.query.createQuestion(db,qid,content,mark,examID)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response

    @app.route("/modifyQuestion",methods=['POST'])
    def modifyQuestion():
        qid=request.form['qid']
        content=request.form['content']
        mark=request.form['mark']
        result=Examination.query.modifyQuestion(db,qid,content,mark)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response
    @app.route("/questionDelete")
    def questionDelete():
        qid=request.args.get('id')
        result=Examination.query.deteleExam(db,qid)
        print(result)
        data = result
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    @app.route("/searchQuestion")
    def searchQuestion():
        content=request.args.get('content')
        result=Examination.query.searchQuestion(db,content)
        listExam = [[x[0],x[1],x[2],x[3]] for x in result]
        data = {
            'name':'Examination',
            'listExam': listExam
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        print(data)
        return response
    return app