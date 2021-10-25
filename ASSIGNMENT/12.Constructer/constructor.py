class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_details(self):
        print("name :", self.name)
        print("age :", self.age)

        
p1 = Person("abhishek",21)
p2 = Person("sanju",50)

p1.print_details()
p2.print_details()
