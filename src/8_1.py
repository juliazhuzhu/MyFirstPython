

class Person:
    def __init__(self, sex, age ):
        self.sex = sex 
        self.age = age 
    
    def getAge(self):
        return self.age
    
    def getSex(self):
        return self.sex
    

class Teacher(Person):
    def __init__(self,sex, age, course):
        super().__init__(sex=sex, age=age)
        self.course = course
    
    def getCourse(self):
        return self.course

class Student(Person):
    def __init__(self,sex, age, grade):
        super().__init__(sex=sex, age=age)
        self.grade = grade 
        
    def getGrade(self):
        return self.grade
    


lucy = Teacher("female",30,"English")
print(lucy.getAge())
print(lucy.getCourse())
print(lucy.getSex())

dory = Student("girl",4,"K3B")
print(dory.getAge())
print(dory.getGrade())
print(dory.getSex())

def getAssitant():
    return "sophy"
setattr(lucy,'getAssistant',getAssitant)

print(lucy.getAssistant())
    
    