class Dicussion():
    def __init__(self,userid,courseid,startdate,content):
        self.startdate=startdate
        self.userid=userid
        self.courseid=courseid
        self.content=content
    
    def __str__(self):
        return str(self.startdate)+" - "+str(self.userid)+" - "+str(self.courseid)+" - "+str(self.content)
    
class query():
    @staticmethod
    def getDicussionList(db,courseid):
        dicussion_list=[]
        sql="exec getlistdicussion {}".format(courseid)
        userid=[]
        courseid=[]
        startdate=[]
        content=[]
        username=[]
        numcomment=[]
        dicid=[]
        result=db.engine.execute(sql)
        result=result.fetchall()
        for item in result:
            userid.append(item[0])
            courseid.append(item[1])
            startdate.append(str(item[2])[:-10])
            content.append(item[3])
            username.append(item[4])
            numcomment.append(item[5])
            dicid.append(item[6])
        res_dict=[{'userid':i,'courseid':c,'startdate':s,'content':a,'username':us,'numcomment':n,'dicid':d} for i,c,s,a,us,n,d in zip(userid,courseid,startdate,content,username,numcomment,dicid)]
        return res_dict

    @staticmethod
    def addDicussion(db,userid,courseid,content):
        sql="exec insert_dicussion {}, {}, N\'{}\'".format(userid,courseid,content)
        connection=db.engine.connect()
        trans=connection.begin()
        result=connection.execute(sql)
        trans.commit()
    
    @staticmethod
    def deleteDicussion(db,dicid):
        sql="delete from dicussion where dicid={}".format(dicid)
        connection=db.engine.connect()
        trans=connection.begin()
        result=connection.execute(sql)
        trans.commit()
    
    @staticmethod
    def getDicussion(db,dicid):
        sql="select dicid,courseid,startdate,content,username from Dicussion join Users on Dicussion.userid=Users.userid where dicid={}".format(dicid)
        result=db.engine.execute(sql)
        result=result.fetchone()
        dicid=result[0]
        courseid=result[1]
        startdate=str(result[2])[:-10]
        content=result[3]
        username=result[4]
        res_dict={'dicid':dicid,'courseid':courseid,'startdate':startdate,'content':content,'username':username}
        return res_dict
    
    @staticmethod
    def checkDicussion(db,dicid):
        sql="select * from dicussion where dicid={}".format(dicid)
        result=db.engine.execute(sql)
        result=result.fetchone()
        if result is None:
            return False
        return True