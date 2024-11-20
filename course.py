import sqlite3
import datetime
from sql import *


class Course:

    def __init__(self, name):
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()

    def get_course(self, course_id):

        result = self.curs.execute(GET_COURSE, (course_id, )).fetchone()
        name = result[0]
        self.name = name
        print(self.name, course_id)

        self.name = name
        self.course_id = course_id

    def create_course(self, name):
        """ Create new course in the courses table """

        self.curs.execute(CREATE_COURSE, (name, ))
        self.conn.commit()
        print("Course created")

    def update_course(self, name, course_id):
        """ Update course name """

        self.curs.execute(UPDATE_COURSE, (name, course_id))
        rowcount = self.curs.rowcount
        self.conn.commit()
        if rowcount == 1:
            print("Course name has been updated")
        else:
            print("No match for that course_id. Please check the course_id is correct")


if __name__ == "__main__":

    cs1 = Course("Python")
    # cs1.create_course("Python")
    cs1.update_course("Networking Concepts", 9)
    # cs1.get_course(1)
    # print(cs1.course_id)