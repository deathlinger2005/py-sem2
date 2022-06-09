# Class in python:  
class Person:
    def setDetails(self, name ,age):
        self.name = name
        self.age = age
    
    def getDetails(self):
        print("The age of {} is {}".format(self.name,self.age))

person1 = Person()
person1.setDetails("Aman",20)
person1.getDetails()
