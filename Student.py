class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
            
    def print_score(self):
        print '%s:%s' %(self.__name,self.__score)
     
    def set_name(self,name):
        self.__name=name
        
    def set_score(self,score):
        self.__score=score
    def get_grade(self):
        if self.__score>90:
            print 'A'
        elif self.__score>60:
            print 'B'
        else:
            print 'C'
        
        
       
        
