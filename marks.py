import sqlite3
import datetime
from sql import *
from course import Course


# Foreign key from two tables

class Marks(Course):

    def __init__(self, course_id, course_name, student_id, student_name, mark, year):
        super().__init__(course_id)
        self.conn = sqlite3.connect('student.db')
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.curs = self.conn.cursor()


        self.student_id = student_id
        self.student_name = student_name
        self.mark = mark
        self.year = year

    def create_mark(self, course_id, course_name, student_id, student_name, mark, year):
        """ Insert a mark with student id and course id into the marks table """

        result = self.curs.execute(CREATE_MARK, (course_id, course_name, student_id, student_name, mark, year))
        self.conn.commit()
        print("Mark inserted")

    def get_marks(self, course_id):
        """ Get one record of marks for one course for one student """

        result = self.curs.execute(GET_MARKS, course_id).fetchone()
        print(result[0])
        print(f"Mark for student id: {self.student_id} is. Course name: {result[0]}, mark is: {result[1]}")



if __name__ == "__main__":

    # stu = Student("James Riley", "21 Main Street, Newry", "1980-01-01")
    m1 = Course("Java")
    m1.get_course(3)
    m2 = Marks(9, "Networking Concepts",  1, "Frank Riley", 70, 1990)
    m2.create_mark(m1.course_id, m1.name, 1, "Frank Riley", 60, 1992)


