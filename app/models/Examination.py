

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

    @staticmethod
    def createExam(db,courseID,examID):
        sql="insert into Examination(courseid,eid,totalMark) values('"+str(courseID)+"','"+str(examID)+"',0)"
        try:
            result = db.engine.execute(sql)
            return {'message': 'success'}
        except:
            return {'message': 'trùng exam id'}
    @staticmethod
    def getAllQuestion(db,examid):
        sql="EXEC danhsachCauHoiCuaKiThi @makythi='"+str(examid)+"'"
        result=db.engine.execute(sql)
        return result

    @staticmethod
    def createQuestion(db,qid,content,mark,examID):
        sql = "EXEC ins_question  @QuestionID = '"+qid+"', @Content = N'"+content+"', @mark ="+mark+", @examID = '"+examID+"';"
        try:
            connection=db.engine.connect()
            trans=connection.begin()
            connection.execute(sql)
            trans.commit()
            return {'message': 'success'}
        except:
            return {'message': 'trùng question id'}

    
    @staticmethod
    def modifyQuestion(db,qid,content,mark):
        sql = "UPDATE Question SET content = N'"+content+"', mark = "+str(mark)+ " WHERE qid = '"+qid+"'; "
        try:
            result = db.engine.execute(sql)
            return {'message': 'success'}
        except:
            return {'message': 'trùng question id'}

    @staticmethod
    def deteleExam(db,qid):
        try:
            sql="delete from Question where qid='"+str(qid)+"'"
            result = db.engine.execute(sql)
            return {'message': 'delete success'}
        except:
            return {'message': 'trùng question id'}
