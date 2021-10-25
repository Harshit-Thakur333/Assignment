class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_person_details(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number = roll_number
    def show_student_details(self):
        print("roll_number",self.roll_number)
class Result(Student):
    def __init__(self,name,age,roll_number,marks1,marks2,marks3):
        super().__init__(name,age,roll_number)
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def show_result_details(self):
        total = self.marks1 + self.marks2 +self.marks3
        percentage = total/300*100
        print("marks of subject1",self.marks1)
        print("marks of subject2",self.marks2)
        print("marks of subject3",self.marks3)
        print("total",total)
        print("percentage",round(percentage,2))

              
r=Result("Harshit",21,210,65,80,98)
r.show_student_details()
r.show_person_details()
r.show_result_details()

    
