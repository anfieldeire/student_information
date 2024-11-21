import sqlite3
import datetime
from sql import *
from student import *


class Degree:

    def __init__(self, degree_id, degree_name, student_id, overall_mark, graduation_year):
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
            print("overall grade")
            print(self.overall_grade)
        elif self.overall_mark >= 50 & self.overall_mark < 60:
            self.overall_grade = "C"
        elif self.overall_mark >= 40 & self.overall_mark < 50:
            self.overall_grade = "D"

        return self.overall_grade

    def create_degree(self, degree_id, degree_name, student_id, overall_mark, graduation_year):
        """ Create a degree table with degree name and student information """

        student_name = Student.get_student(student_id)
        if student_name is None:
            print("Error")
            return
        else:
            overall_grade = self.set_grade(overall_mark)

            print("in create degree")
            print(f"Grade: {overall_grade}")
            print(f"Name: {student_name}")
            print({degree_id}, {degree_name}, {student_id}, {student_name}, {overall_mark}, {graduation_year},
            {overall_grade})
            self.curs.execute(CREATE_DEGREE, (degree_id, degree_name, student_id, student_name, overall_mark, graduation_year,
                                              overall_grade))

            print("Degree has been created")
        self.conn.commit()




if __name__ == "__main__":

    # d1 = Degree(3, "Bsc Business & Computing", 2,  60, "1992")
    # d1.create_degree(3, "Bsc Business & Computing", 2, 60, "1992")
    d2 = Degree(7, "TEST", 19,  60, "1992")
    d2.create_degree(7, "TEST", 19, 60, "1992")


