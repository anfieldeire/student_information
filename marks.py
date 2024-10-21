import sqlite3
import datetime
from sql import *
from student import Student

# Inherit from Student and Course

class Marks(Student):

    def __init__(self, course_id, course_name, student_id, student_name, mark, year):
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()
        self.course_id = course_id
        self.course_name = course_name
        self.student_id = student_id
        self.student_name = student_name
        self.mark = mark
        self.year = year

    def create_mark(self, course_id, course_name, student_id, student_name, mark, year):
        """ Insert a mark with student id and course id into the marks table """

        result = self.curs.execute(CREATE_MARK, (course_id, course_name, student_id, student_name, mark, year))
        self.conn.commit()
        print("Mark inserted")

    def get_marks(self, course_id, student_id):
        """ Get one record of marks for one course for one student """

        result = self.curs.execute(GET_MARKS, (course_id, student_id)).fetchone()
        print(result[0])
        print(f"Mark for student id: {self.student_id} is. Course name: {result[0]}, mark is: {result[1]}")



if __name__ == "__main__":


    m1 = Marks(1, "Networking Concepts", 1, "Frank Riley", 70, 1990)
    # m1.create_mark(1, "Networking Concepts", 1, "Frank Riley", 70, 1990)
    m1.get_marks(1, 1)
