class Student(object):
    def __init__(self,name):
        self.__name=name
        
    def __call__(self):
        print self.__name