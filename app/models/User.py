

class Users():
    pass
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

        query.insertrole(db,userid,role)
    
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
        print('abc')
        print(error.fetchone())
        trans.commit()

    




