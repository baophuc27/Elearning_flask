class Enroll:
    pass
class query:
    @staticmethod
    def addEnroll(db,studentid,courseid):
        sql="exec insert_enroll {},{}".format(studentid,courseid)
        connection=db.engine.connect()
        trans=connection.begin()
        result=connection.execute(sql)
        trans.commit()
    
    def checkEnroll(db,studentid,courseid):
        sql="SELECT dbo.check_enroll({},{})".format(studentid,courseid)
        result=db.engine.execute(sql)
        result=result.fetchone()
        if result[0]==0:
            return False
        return True
        