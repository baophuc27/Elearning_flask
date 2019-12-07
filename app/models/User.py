

class Users():
    def __init__(self,userid,uname,sex,bdate,username):
        self.userid=userid
        self.uname=uname
        self.sex=sex
        self.bdate=bdate
        self.username=username

class query():
    @staticmethod
    def getNameandPass(db,name,password):
        sql="select dbo.checklogin (\'"+name +"\', \'" + password +"\')" 
        result = db.engine.execute(sql)
        result = result.fetchone()
        if result[0] == True:
            return True
        else:
            return False

    @staticmethod
    def addsession(db,name):
        sql = "select * from Users where (uname=\'"+name+"\')"
        result = db.engine.execute(sql)
        result = result.fetchone()
        print("RESULT {0}".format(result))
        return result

    @staticmethod
    def checkifnameregisted(db,name):
        sql="select dbo.checknameregisted (\'"+name + "\')" 
        result = db.engine.execute(sql)
        result = result.fetchone()
        if result[0] == True:
            return True
        else:
            return False

    @staticmethod
    def createnewuser(db,uname,sex,bdate,address,password,username,role):
        if address=='':
            sql="exec dbo.insertinuser \'"+uname+"\',\'"+sex+"\',\'"+bdate+"\',NULL,\'"+password+"\',N\'"+username+"\'"
        else:
            sql="exec dbo.insertinuser \'"+uname+"\',\'"+sex+"\',\'"+bdate+"\',N\'"+address+"\',\'"+password+"\',N\'"+username+"\'"
        connection=db.engine.connect()
        trans=connection.begin()
        connection.execute(sql)
        trans.commit()
        # select id of new user
        sql="select userid from Users where (uname=\'"+uname+"\')"
        result=db.engine.execute(sql)
        userid=result.fetchone()
        userid=userid[0]
        return query.insertrole(db,userid,role)
    
    @staticmethod
    def insertrole(db,userid,role):
        #add into teacher or student
        if role=='Student':
            sql="exec dbo.insertinstudent "+str(userid)+",'T',NULL,NULL"
        else:
            sql="exec dbo.insertinteacher "+str(userid)+",NULL"
        connection=db.engine.connect()
        trans=connection.begin()
        error=connection.execute(sql)
        trans.commit()
        
        sql="select userid from Users where (userid="+str(userid)+")"
        result=db.engine.execute(sql)
        userid=result.fetchone()
        if (userid is None):
            return False
        else:
            return True
    

    @staticmethod
    def addphone(db,uname,phones):
        flag= True
        for x in phones:
            sql="select dbo.checkphone (\'"+x+"\')" 
            result = db.engine.execute(sql)
            result = result.fetchone()
            if result[0] == False:
                flag= False
        if flag == False:
            return False
        else:
            for x in phones:
                sql="exec dbo.insertinphone \'"+uname + "\',\'"+x+"\'" 
                connection=db.engine.connect()
                trans=connection.begin()
                connection.execute(sql)
                trans.commit()
        return True

    @staticmethod 
    def searchteacher (db,name,orderby,range):
        sql="exec dbo.searchbynameteacher N\'"+name + "\',\'"+orderby+"\',"+str(range) 
        result = db.engine.execute(sql)
        result = result.fetchall()
        return result

    @staticmethod
    def searchstudent (db,name,orderby):
        sql="exec dbo.searchbynamestudent N\'"+name + "\',\'"+orderby+"\'"
        result = db.engine.execute(sql)
        result = result.fetchall()
        return result

    @staticmethod
    def deleteuser(db,userid):
        sql="delete from Users where (userid="+str(userid)+")"
        connection=db.engine.connect()
        trans=connection.begin()
        connection.execute(sql)
        trans.commit()


