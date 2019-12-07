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


    @app.route("/editbutton",methods=['GET'])
    def edituser():
        userid = request.args.get('data-id')
        if (session[0].uname)!='admin':
            flash('You dont have permission to edit user')
            return render_template('home.html')
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
        if (not User.query.checkcanupdate(db,userid,displayname,sex,birthday,address)):
            flash('Wrong information')
            return render_template('home.html')
        if not User.query.update(db,userid,displayname,sex,birthday,address):
            flash('Teacher must be over 18')
            return render_template('home.html')
        flash('Edit success')
        return render_template("edit.html")




    

    return app


