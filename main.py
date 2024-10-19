import sqlite3
import datetime
from sql import *

#conn = sqlite3.connect("C:\\Users\\hassy\\PycharmProjects\\student\\pythonProject\\.venv\\Scripts\\student.db")

# conn = sqlite3.connect('student.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
# print("Connected")
# curs = conn.cursor()
# conn = sqlite3.connect('student.db')
# curs = conn.cursor()

class Student:

    def __init__(self, name, home_address, dob):
        self.name = name
        self.home_address = home_address
        self.dob = dob
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()

    def create_student(self, name, home_address, dob):
        """ Insert student record into dob. student_id will be generated automatically """

        with conn:
            result = curs.execute(CREATE_STUDENT, (name, home_address, dob))
            print(f"Student record created. Student id: {result.lastrowid}")

    def get_student(self, student_id):
        """ Query student table for student information based on the student id provided """

        result = self.curs.execute(GET_STUDENT, student_id)
        print(f" Student Information listed here:  {list(result)}")

    def update_student(self, name, home_address, student_id):
        """ Update name and or address for students """
        # with conn:
        result = self.curs.execute(UPDATE_STUDENT, (name, home_address, student_id))
        rowcount = self.curs.rowcount
        self.conn.commit()
        if rowcount == 1:
            print("Student has been updated")
        else:
            print("Student record has not been updated. Please check the data and student id are correct")

    def create_course(self, name, course_id):
        result




if __name__ == "__main__":

    # James = Student("James Riley", "20 Main Street, Newry", "1980-01-01 ")
    # James.create_student("James Riley", "20 Main Street, Newry", "1980-01-01")
    stu = Student("James Riley", "21 Main Street, Newry", "1980-01-01")
    # stu.create_student("James Riley", "20 Main Street, Newry", "1980-01-01")
    stu.get_student("1")
    # stu.update_student( "Frank Riley", "16 Main Street Newry", 1)
    stu.update_student("Frank Riley", "16 Main Street Newry", 9)






