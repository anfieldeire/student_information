import sqlite3
import datetime
from sql import *

#conn = sqlite3.connect("C:\\Users\\hassy\\PycharmProjects\\student\\pythonProject\\.venv\\Scripts\\student.db")

conn = sqlite3.connect('student.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
print("Connected")
curs = conn.cursor()


class Student:

    def __init__(self, name, home_address, dob):
        self.name = name
        self.home_address = home_address
        self.dob = dob

    def create_student(self, name, home_address, dob):
        """ Insert student record into dob. student_id will be generated automatically """

        with conn:
            result = curs.execute(CREATE_STUDENT, (name, home_address, dob))
            print(f"Student record created. Student id: {result.lastrowid}")

    def get_student(self, student_id):

        with conn:
            (result) = curs.execute(GET_STUDENT, student_id)
            # print(f"Student Information {result}")
            print(list(result))




if __name__ == "__main__":

    # James = Student("James Riley", "20 Main Street, Newry", "1980-01-01 ")
    # James.create_student("James Riley", "20 Main Street, Newry", "1980-01-01")
    stu = Student("James Riley", "20 Main Street, Newry", "1980-01-01")
    # stu.create_student("James Riley", "20 Main Street, Newry", "1980-01-01")
    stu.get_student("1")






