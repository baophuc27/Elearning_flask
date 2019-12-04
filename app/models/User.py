

class Users():
    pass
class query():
    @staticmethod
    def getNameandPass(db,name,password):
        sql="select * from users where uname=\'"+name+ "\' and password=\'"+password +"\'"
        result = db.engine.execute(sql)
        if result is not None:
            return True
        else:
            return False




