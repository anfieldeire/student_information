import sqlite3
import datetime
from sql import *
from student import *


class Degree:

    def __init__(self, degree_name, student_id, overall_mark, graduation_year, overall_grade):
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()

        self.degree_name = degree_name
        self.student_id = student_id
        self.overall_mark = overall_mark
        self.graduation_year = graduation_year
        self.overall_grade = overall_grade

    def create_degree(self, degree_name, student_id, overall_mark, graduation_year, overall_grade):
        """ Create a degree table with degree name and student information """

        student_name = get_student(student_id)
        print("student name")
        print(student_name)

        self.curs.execute(CREATE_DEGREE, (degree_name, student_id, student_name, overall_mark, graduation_year,
                                          overall_grade))
        var = (degree_name, student_id, student_name, overall_mark, graduation_year, overall_grade)
        print("var")
        print(var)
        self.conn.commit()

if __name__ == "__main__":

    d1 = Degree("Bsc Hons Computing", 2,  70, "1995", "A")
    d1.create_degree("Bsc Hons Computing", 2, 70, "1995", "A")



