class Student(object):
    __slots__=('name','age')
    def print_score(self):
        print self.age
        
class GraduateStudent(Student):
    pass
        
    