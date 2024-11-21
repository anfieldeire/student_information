import sqlite3
import datetime
from sql import *


# conn = sqlite3.connect('student.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

class Student:

    def __init__(self, name, home_address, dob):
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()

        self.name = name
        self.home_address = home_address
        self.dob = dob

    def create_student(self, name, home_address, dob):
        """ Insert student record into dob. student_id will be generated automatically """

        result = self.curs.execute(CREATE_STUDENT, (name, home_address, dob))
        self.conn.commit()
        print(f"Student record created. Student id: {result.lastrowid}")

    def update_student(self, name, home_address, student_id):
        """ Update name and or address for students """

        self.curs.execute(UPDATE_STUDENT, (name, home_address, student_id))
        rowcount = self.curs.rowcount
        self.conn.commit()
        if rowcount == 1:
            print("Student has been updated")
        else:
            print("Student record has not been updated. Please check the data and student id are correct")

    def get_student(student_id):
        """ Query student table for student information based on the student id provided """

        conn = sqlite3.connect('student.db')
        curs = conn.cursor()

        result = curs.execute(GET_STUDENT, (student_id, )).fetchone()
        rowcount = curs.rowcount
        if rowcount < 1:
            print("Student not found")
        else:
            student_name = result[0]
        # print(student_name)
        # print(f" Student Information listed here:  {list(result)}")
        # print(type(student_name))
        # print(type(result[1]))

            return student_name


# if __name__ == "__main__":

    # stu = Student("James Tobey", "21 Main Street, Newry", "1980-01-01")
    # # stu.create_student("Paul McStay", "22 Main Street, Newry", "1960-01-01")
    # # stu.update_student("Frank Riley", "17 Main Street Newry", 1)
    # get_student(2)






