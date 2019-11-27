class User(object):
    name:str
    age:int
    def __init__(self,name=None,age=None):
        self.__name=name
        self.__age=age

    def set_name(self,name):
        self.__name=name

    def get_name(self,name):
        return self.__name
    
    def set_age(self,age):
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def __str__(self):
        return self.__name+" - "+str(self.__age)



