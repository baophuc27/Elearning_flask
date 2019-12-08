class Course():
    def __init__(self,courseid,cname,cdesc,rate,price):
        self.courseid=courseid
        self.cname=cname
        self.cdesc=cdesc
        self.rate=rate
        self.price=price
    
    def __str__(self):
        return self.courseid+" - "+self.cname+" - "+self.cdesc+" - "+self.rate+" - "+self.price

class Query():
    @staticmethod
    def getdataCourse(db):
        sql = "select * from Course "
        result = db.engine.execute(sql)
        result = result.fetchall()
        courseId=[]
        cname=[] 
        cdesc=[] 
        price=[]
        rate=[]
        for index in result:
            courseId.append(index[0])
            cname.append(index[1])
            cdesc.append(index[2])
            price.append(str(index[3]))
            rate.append(str(index[4]))
        lstData = [{"courseId": Id,"cname": name,"cdesc": desc,"price": fee,"rate": rank}  for Id, name, desc, fee, rank in zip(courseId, cname, cdesc, price, rate)]  
        return lstData
    
    
    def getdataLesson(db,courseId):
        sql = "EXEC Query_Course_Lesson_By_Id "+str(courseId)
        result = db.engine.execute(sql)
        result = result.fetchall()
        lid=[]
        lname=[] 
        for index in result:
            lid.append(index[0])
            lname.append(index[1])
        lstLesson = [{"lid": Id,"lname": name}  for Id, name in zip(lid, lname)]  
        return lstLesson
    
    def getdataCurriculum(db):
        sql = "select * from Curriculum "
        result = db.engine.execute(sql)
        result = result.fetchall()
        currid=[]
        curriname=[] 
        curdesc=[] 
        for index in result:
            currid.append(index[0])
            curriname.append(index[1])
            curdesc.append(index[2])
        lstData = [{"currid": Id,"curriname": name,"curdesc": desc}  for Id, name, desc in zip(currid, curriname, curdesc)]  
        return lstData
    

    def getdataTopic(db):
        sql = "select * from Topic "
        result = db.engine.execute(sql)
        result = result.fetchall()
        tid=[]
        tname=[] 
        tdesc=[] 
        for index in result:
            tid.append(index[0])
            tname.append(index[1])
            tdesc.append(index[2])
        lstData = [{"tid": Id,"tname": name,"tdesc": desc}  for Id, name, desc in zip(tid, tname, tdesc)]  
        return lstData
    
    def searchCurriculum(db,curriname):
        sql = "EXEC Query_3 N\'"+str(curriname)+"\'"
        result = db.engine.execute(sql)
        result = result.fetchall()
        cname=[]
        price=[] 
        for index in result:
            cname.append(index[0])
            price.append(str(index[1]))
        lstData = [{"cname": name,"price": fee}  for name, fee in zip(cname, price)]  
        return lstData
    
    def calculateCurriculum(db,curriname):
        sql = "SELECT dbo.count_fee(N\'"+str(curriname)+"\')"
        result = db.engine.execute(sql)
        result = result.fetchone()
        return result[0]
    
    def searchTopic(db,topicname):
        sql = "EXEC Query_1 N\'"+str(topicname)+"\'"
        result = db.engine.execute(sql)
        result = result.fetchall()
        tname=[]
        price=[] 
        for index in result:
            tname.append(index[0])
            price.append(str(index[1]))
        lstData = [{"tname": name,"price": fee}  for name, fee in zip(tname, price)]  
        return lstData

    def calculateCourse_Time(db,coursename):
        sql = "SELECT dbo.Calculate_Time(N\'"+str(coursename)+"\')"
        result = db.engine.execute(sql)
        result = result.fetchone()
        return result[0]
    
    def search(db,number):
        sql = "EXEC Query_2 "+str(number)
        result = db.engine.execute(sql)
        result = result.fetchall()
        cname=[]
        camount=[] 
        for index in result:
            cname.append(index[0])
            camount.append(index[1])
        lstData = [{"cname": name,"camount": amount}  for name, amount in zip(cname, camount)]  
        return lstData
    
    
    
        
        
        

