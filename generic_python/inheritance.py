#Refresher into inheritance 

class Person(object):
    def __init__(self, name:str, age:int,*args,**kwargs):
        print("Inside Person init")
        self.name = name
        self.age = age
    def getDetails(self):
        print("PERSON DETAILS")
        print("Name : ",self.name)
        print("Age : ",str(self.age))

class Employee(Person):
    def __init__(self, name:str, age:int, empid:int,*args,**kwargs):
        print("Inside Employee init")
        super().__init__(name,age,*args,**kwargs)
        self.empid = empid
    def getDetails(self):
        print("EMPLOYEE DETAILS")
        super().getDetails()
        print("Empid : ",str(self.empid))

class Student(Person):
    def __init__(self, name:str, age:int, university:str,course_name:str,*args,**kwargs):
        print("Inside Student init")
        super().__init__(name,age,*args,**kwargs)
        self.university = university
        self.course_name = course_name
    def getDetails(self):
        print("STUDENT DETAILS")
        super().getDetails()
        print("University : ",str(self.university))
        print("Course Name : ",str(self.course_name))
class PartTimeEmployee(Student,Employee):
    def __init__(self, name:str, age:int, university:str,course_name:str, empid:int, hours:float,*args,**kwargs):
        print("Inside Part Time Emp init")
        super().__init__(name = name,age = age,university = university,course_name = course_name,empid= empid,*args,**kwargs)
        self.hours = hours
    def getDetails(self):
        print("PART_TIME EMPLOYEE DETAILS")
        Student.getDetails(self)
        Employee.getDetails(self)
        print("Hours : ",str(self.hours))



if __name__ == '__main__':
    emp = PartTimeEmployee("akr",30 ,"UVIC","Python",123456,25.0)
    emp.getDetails()
