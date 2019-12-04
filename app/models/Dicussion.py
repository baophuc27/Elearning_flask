class Dicussion():
    def __init__(self,tid,startdate,userid,courseid,content):
        self.tid=tid
        self.startdate=startdate
        self.userid=userid
        self.courseid=courseid
        self.content=content
    
    def __str__(self):
        return self.tid+" - "+self.startdate+" - "+self.userid+" - "+self.courseid+" - "+self.content
    
class query():
    @staticmethod
    def getDicussionList(db):
        dicussion_list=[]
        sql="select tid,startdate,userid,courseid,content from Dicussion"
        result=db.engine.execute(sql)
        for item in result:
            tid=item[0]
            startdate=item[1]
            userid=item[2]
            courseid=item[3]
            content=item[4]
            dicussion=Dicussion(tid,startdate,userid,courseid,content)
            dicussion_list.append(dicussion)
        for dicuss in dicussion_list:
            print(dicuss)
    @staticmethod
    def addDicussion(db):
        sql="insert into Dicussion values "