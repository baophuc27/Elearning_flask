

class Users():
    pass
class query():
    @staticmethod
    def getListFName(db):
        sql="select fname from employee"
        result=db.engine.execute(sql)
        names=[row[0] for row in result]
        print(names)


