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
    GPA = 0.00
    Grade_Level = 0
    Student_ID = "18"

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


staff = User()
staff.LoginInfo()

student = Student()
student.LoginInfo()

teacher = Teacher()
teacher.LoginInfo()
