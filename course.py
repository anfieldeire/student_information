import sqlite3
import datetime
from sql import *


class Course:

    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()

    def create_course(self, name):
        """ Create new course in the courses table """

        result = self.curs.execute(CREATE_COURSE, (name, ))
        self.conn.commit()
        print("Course created")


if __name__ == "__main__":

    cs1 = Course("Networking Advanced")
    cs1.create_course("Networking Advanced")