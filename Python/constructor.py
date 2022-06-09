# __Constructor__ in python:
class Person:
    '''This is a DocString'''
    docStr = '''This is a DocString inside class variable'''
    def __init__(s,n,a):
        s.name = n
        s.age = a

    def getDetails(s):
        print('The age of {} is {}'.format(s.name,s.age))


person1 = Person('Ayush',21)
person1.getDetails()

# Showing object of instance variable:

print(person1.__dict__)

# Showing document string:

print(Person.__doc__)
print(Person.docStr)