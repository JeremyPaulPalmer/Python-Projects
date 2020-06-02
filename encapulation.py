# Python Ver:   3.8.2
#
# Purpose:      Inheritance Assignment #2




class User:
    name = 'Jeremy Palmer'
    email = 'duxfan18@gmail.com'
    phone_number = '5037018554'
    password = 'TechAcademy'

    def LoginInfo(self):
        input_name = input("Please enter your name: ")
        input_email = input("Please enter your email: ")
        input_pw = input("Please enter your password: ")
        if (input_email == self.email and input_pw == self.password):
            print("Welcome back, {}!".format(input_name))
        else:
            print("Please re-enter your login credentials.")

class Student(User):
    Grade_Level = 0
    Student_ID = "18"

    def __init__(self):
        self._GPA = 0.00
        self.__Student_ID = "18"

    def getPrivate(self):
        print(self.__Student_ID)

    def setPrivate(self, private):
        self.__Student_ID = private

    def LoginInfo(self):
        input_name = input("Please enter your name: ")
        input_email = input("Please enter your email: ")
        input_pw = input("Please enter your password: ")
        input_ID = input("Please enter your Student ID: ")
        if (input_email == self.email and input_pw == self.password and input_ID == self.Student_ID):
            print("Welcome back, {}!".format(input_name))
        else:
            print("Please re-enter your login credentials.")

class Teacher(User):
    Room = 0
    Grade = 0
    Teacher_ID = 0

    def LoginInfo(self):
        input_ID = input("Please enter your Teacher ID: ")
        input_pw = input("Please enter your password: ")
        if (input_ID == self.Teacher_ID and input_pw == self.password):
            print("Welcome back, {}!".format(self.name))
        else:
            print("Please re-enter your login credentials.")


obj = Student()
obj._GPA = 3.89
print(obj._GPA)

obj2 = Student()
obj2.getPrivate()
obj.setPrivate("17")
obj.getPrivate()
