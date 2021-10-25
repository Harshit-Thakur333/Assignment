class XYZ:
     def __init__(self, name, age):
           self.XYZName = name
           self.XYZAge = age   
     def displayAge(self):
           print("Age: ", self.XYZAge)
obj = XYZ("Harshit", 21)
print("Name: ", obj.XYZName)
obj.displayAge()