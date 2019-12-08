class query():
    @staticmethod
    def addComment(db,dicid,content,userid):
        sql="exec insert_comment {}, N\'{}\', {}".format(dicid,content,userid)
        connection=db.engine.connect()
        trans=connection.begin()
        result=connection.execute(sql)
        trans.commit()
    
    @staticmethod
    def getListComment(db,dicid):
        sql="exec get_list_comment {}".format(dicid)
        dicid=[]
        commentid=[]
        content=[]
        ctime=[]
        username=[]
        result=db.engine.execute(sql)
        result=result.fetchall()
        for item in result:
            dicid.append(item[0])
            commentid.append(item[1])
            content.append(item[2])
            ctime.append(str(item[3])[:-10])
            username.append(item[4])
        res_dict=[{'dicid':d,'commentid':c,'content':ct,'time':t,'username':u} for d,c,ct,t,u in zip(dicid,commentid,content,ctime,username)]
        return res_dict
    
    @staticmethod
    def deleteComment(db,commentid):
        sql="delete from Comment where commentid={}".format(commentid)
        connection=db.engine.connect()
        trans=connection.begin()
        result=connection.execute(sql)
        trans.commit()
    
