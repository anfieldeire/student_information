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

        result = self.curs.execute(CREATE_COURSE, (name, ))
        self.conn.commit()
        print("Course created")

    # def get_course(self, course_id):
    #
    #     result = self.curs.execute(GET_COURSE, (course_id, )).fetchone()
    #     name = result[0]
    #     self.name = name
    #     self.course_id = course_id
    #     print(self.name, course_id)
    #     return name, course_id


    def update_course(self, name, course_id):
        """ Update course name """

        result = self.curs.execute(UPDATE_COURSE, (name, course_id))
        self.conn.commit()
        print("Course updated")


if __name__ == "__main__":

    cs1 = Course("Networking Advanced")
    # cs1.create_course("Networking Advanced")
    # cs1.update_course("Networking Concepts", 1)
    cs1.get_course(1)
    print(cs1.course_id)