from flask import *
from flask_sqlalchemy import SQLAlchemy
from .models import User,Dicussion,Comment
from .models import User
from .models import Course
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
                return render_template("main.html")
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
                flash("""Your display name must be greater than 3 and less than 30.\n 
                Your username must be less than 20 and greater than 3.\n
                Length of address must be less than 30.\n
                Day of birthday must be less than now.\n
                Teacher must be over 18 years old""")
                return render_template("register.html")
            if phones!=['']:
                if (not User.query.addphone(db,name,phones)):
                    flash("Phones less than 9 digits")
                    return render_template("register.html")
            return render_template("index.html")

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


    @app.route("/searchstudent",methods=["POST"])
    def searchstudent():
        name = request.form['name']
        order = request.form['order']
        if name=='':
            flash('Please fill out name to search')
            return render_template('studentlist.html')
        result = User.query.searchstudent(db,name,order)
        return render_template('studentlist.html',data=result)

    
    @app.route("/delbuttonstudent",methods=['GET'])
    def deluserstudent():
        userid = request.args.get('data-id')
        if (session[0].uname)!='admin':
            flash('You dont have permission to delete user')
            return render_template('studentlist.html')
        User.query.deleteuser(db,userid)
        flash('Delete user success')
        return render_template('studentlist.html')


    @app.route("/delbuttonteacher",methods=['GET'])
    def deluserteacher():
        userid = request.args.get('data-id')
        if (session[0].uname)!='admin':
            flash('You dont have permission to delete user')
            return render_template('teacherlist.html')
        User.query.deleteuser(db,userid)
        flash('Delete user success')
        return render_template('teacherlist.html')

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

    @app.route("/editbutton",methods=['GET'])
    def edituser():
        userid = request.args.get('data-id')
        if (session[0].uname)!='admin':
            flash('You dont have permission to edit user')
            return render_template('main.html')
        nameuser = User.query.getuname(db,userid)
        return render_template('edit.html',data=nameuser,id=userid)


    
    @app.route("/edituser/",methods=['POST'])
    def editupdateuser():
        userid = request.args.get('data-id')
        displayname = request.form['username']
        sex = request.form['GENDER']
        if sex =='Male':
            sex= 'M'
        else:
            sex = 'F'
        birthday = request.form['myDate']
        address= request.form['address']
        phones = request.form['phone'] 
        phones = phones.split(',')
        User.query.dropphone(db,userid)
        nameuser = User.query.getunamelogin(db,userid)
        if phones!=['']:
            if (not User.query.addphone(db,nameuser,phones)):
                flash("Phones less than 9 digits")
                nameuser = User.query.getuname(db,userid)
                return render_template('edit.html',data=nameuser,id=userid)
        if (not User.query.checkcanupdate(db,userid,displayname,sex,birthday,address)):
            flash('Wrong information')
            nameuser = User.query.getuname(db,userid)
            return render_template('edit.html',data=nameuser,id=userid)
        if not User.query.update(db,userid,displayname,sex,birthday,address):
            flash('Teacher must be over 18')
            nameuser = User.query.getuname(db,userid)
            return render_template('edit.html',data=nameuser,id=userid)
        flash('Edit success')
        nameuser = User.query.getuname(db,userid)
        return render_template('edit.html',data=nameuser,id=userid)
    


  



    

    return app
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

