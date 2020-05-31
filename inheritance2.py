# Python Ver:   3.8.2
#
# Purpose:      Inheritance Assignment #2




class User:
    name = 'No Name'
    email = ' '
    phone_number = ' '
    password = ' '

    def LoginInfo(self):
        input_email = input("Please enter your email: ")
        input_pw = input("Please enter your password: ")
        if (input_email == self.email and input_password == self.password):
            print("Welcome back, {}!".format(input_name))
        else:
            print("Please re-enter your login credentials.")

class Student(User):
    GPA = 0.00
    Grade_Level = 0
    Student_ID = 0

    def LoginInfo(self):
        input_ID = input("Please enter you Student ID: ")
        input_pw = input("Please enter your password: ")
        if (input_ID == self.Student_ID and input_pw == self.password):
            print("Welcome back, {}!".format(self.name))
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
