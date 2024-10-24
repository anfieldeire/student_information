import sqlite3
import datetime
from sql import *
from student import *


class Degree:

    def __init__(self, degree_name, student_id, overall_mark, graduation_year):
        self.conn = sqlite3.connect('student.db')
        self.curs = self.conn.cursor()

        self.degree_name = degree_name
        self.student_id = student_id
        self.overall_mark = overall_mark
        self.graduation_year = graduation_year


    def set_grade(self, overall_mark):
        if self.overall_mark >= 70:
            self.overall_grade = "A"
        elif self.overall_mark >= 60 & self.overall_mark < 70:
            self.overall_grade = "B"
            print("overall grade1")
            print(self.overall_grade)
        elif self.overall_mark >= 50 & self.overall_mark < 60:
            self.overall_grade = "C"
        elif self.overall_mark >= 40 & self.overall_mark < 50:
            self.overall_grade = "D"

        return self.overall_grade


    def create_degree(self, degree_name, student_id, overall_mark, graduation_year):
        """ Create a degree table with degree name and student information """

        student_name = get_student(student_id)
        overall_grade = self.set_grade(overall_mark)

        print("in create degree")
        print(overall_grade)
        self.curs.execute(CREATE_DEGREE, (degree_name, student_id, student_name, overall_mark, graduation_year,
                                          overall_grade))

        print("Degree has been created")
        self.conn.commit()




if __name__ == "__main__":

    d1 = Degree("Bsc Business & Computing", 2,  60, "1992")
    d1.create_degree("Bsc Business & Computing", 2, 60, "1992")



