from flask import *
from flask_sqlalchemy import SQLAlchemy
from .models import User,Dicussion,Comment
from config import app_config
import json
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
                session['user']=User.Users(1,'baophuc','M','27/10/1999','Bảo Phúc').__dict__
                print(session['user'])
                print(session['user']['username'])
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
        return render_template("dicussion.html")
    
    @app.route("/adddicussion")
    def addDicussion():
        userid=request.args.get('userid')
        courseid=request.args.get('courseid')
        content=request.args.get('content')
        session['courseid']=courseid
        Dicussion.query.addDicussion(db,userid,courseid,content)
        dicussion_list=[]
        dicussion_list=Dicussion.query.getDicussionList(db,courseid)
        json_data=json.dumps(dicussion_list)
        json_data1=json.loads(json_data)
        return render_template("dicussion.html",dicussion_list=json_data1)
    
    @app.route("/getlistdicussion")
    def getListDicussion():
        courseid=request.args.get('courseid')
        session['courseid']=courseid
        dicussion_list=[]
        dicussion_list=Dicussion.query.getDicussionList(db,courseid)
        json_data=json.dumps(dicussion_list)
        json_data1=json.loads(json_data)
        return render_template("dicussion.html",dicussion_list=json_data1)

    @app.route("/addcomment")
    def addComment():
        dicid=request.args.get('dicid')
        userid=request.args.get('userid')
        content=request.args.get('content')
        courseid=session['courseid']
        dicussion_list=[]
        Comment.query.addComment(db,dicid,content,userid)
        dicussion_list=Dicussion.query.getDicussionList(db,courseid)
        json_data=json.dumps(dicussion_list)
        json_data1=json.loads(json_data)
        return render_template("dicussion.html",dicussion_list=json_data1)

    @app.route("/deletedicussion")
    def deletedicussion():
        dicid=request.args.get('dicid')
        Dicussion.query.deleteDicussion(db,dicid)
        courseid=session['courseid']
        dicussion_list=[]
        dicussion_list=Dicussion.query.getDicussionList(db,courseid)
        json_data=json.dumps(dicussion_list)
        json_data1=json.loads(json_data)
        return render_template("dicussion.html",dicussion_list=json_data1)

    @app.route("/viewcomment")
    def viewcomment():
        dicid=request.args.get('dicid')
        session['dicid']=dicid
        dicuss=Dicussion.query.getDicussion(db,dicid)
        json_data=json.dumps(dicuss)
        dicuss=json.loads(json_data)
        comment_list=Comment.query.getListComment(db,dicid)
        json_data=json.dumps(comment_list)
        comment_list=json.loads(json_data)
        return render_template("comment.html",comment_list=comment_list,dicuss=dicuss)

    @app.route("/deletecomment")
    def deletecomment():
        commentid=request.args.get('commentid')
        Comment.query.deleteComment(db,commentid)
        dicid=session['dicid']
        dicuss=Dicussion.query.getDicussion(db,dicid)
        json_data=json.dumps(dicuss)
        dicuss=json.loads(json_data)
        comment_list=Comment.query.getListComment(db,dicid)
        json_data=json.dumps(comment_list)
        comment_list=json.loads(json_data)
        return render_template("comment.html",comment_list=comment_list,dicuss=dicuss)

    #-------------HET BAO PHUC-----------------
    return app


