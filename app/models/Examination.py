

class Examination():
    pass
class query():
    @staticmethod
    def getAllExam(db,courseID):
        sql="select * from Examination where courseid="+str(courseID)
        result = db.engine.execute(sql)
        result = result.fetchall()
        return result

    @staticmethod
    def deteleExam(db,examID):
        sql="delete from Examination where eid='"+str(examID)+"'"
        result = db.engine.execute(sql)
        return result



