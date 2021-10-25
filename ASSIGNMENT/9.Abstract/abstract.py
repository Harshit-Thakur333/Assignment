class Person():
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city= city
    def show_details(self):
        print("name",self.name)
        print("age",self.age)
        print("city", self.city)
    def change_city(self,city):
        self.city = city
p1 = Person("Harshit",22,"delhi")
p2 =Person("Kumar",21,"noida")
p1.show_details()
p2.show_details()
p1.change_city("bihar")
p1.show_details()
p2.show_details()
