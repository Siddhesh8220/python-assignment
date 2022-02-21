class InvalidName(Exception):
    pass
class InvalidAge(Exception):
    pass
class InvalidEmail(Exception):
    pass
class InvalidPhone(Exception):
    pass

class Person:
    def __init__(self, name,age,email,phone):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone

def validate(p):
    flag = False

    try:
        if(p.name==""):
            raise InvalidName
    except InvalidName:
        print("Invalid Name!")
        flag = True

    try:
        if(p.age>100 or p.age<10):
            raise InvalidAge
    except InvalidAge:
        print("Invalid Age!")
        flag=True

    try:
        if('@' not in p.email or p.email==''):
            raise InvalidEmail
    except InvalidEmail:
        print("Invalid Email!")
        flag=True

    try:
        if(len(str(p.phone))<10):
            raise InvalidPhone 
    except InvalidPhone:
        print("Invalid Phone!")
        flag=True

    return flag
   

#input
name=input("Enter Name:")
age=int(input("Enter age:"))
email=input("Enter email:")
phone=int(input("Enter Phone number:"))

person = Person(name,age,email,phone)
flag = validate(person)

#global array
Person=list()
if(flag==False):
    Person.append(person)
    print("Object Appended into a global Array!")