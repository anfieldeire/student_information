import sqlite3


conn = sqlite3.connect('student.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES )
curs = conn.cursor()


# https://www.geeksforgeeks.org/python-sqlite-working-with-date-and-datetime/

def create_tables():

    # with conn:
    #     curs.execute(""" CREATE TABLE IF NOT EXISTS student (
    #     name text,
    #     student_id integer PRIMARY KEY,
    #     home_address text,
    #     dob text)""")
    #
    # with conn:
    #     curs.execute(""" CREATE TABLE IF NOT EXISTS courses (
    #     name text,
    #     course_id integer PRIMARY KEY)""")

    # with conn:
    #
    #     curs.execute(""" CREATE TABLE IF NOT EXISTS marks (
    #     course_id integer,
    #     course_name text,
    #     student_id integer,
    #     student_name text,
    #     mark integer,
    #     year text,
    #     foreign key (student_id) references student (student_id),
    #     foreign key (course_id) references courses (course_id),
    #     primary key (student_id, course_id))
    #     """)

    # with conn:
    #     curs.execute(""" CREATE TABLE IF NOT EXISTS grades (
    #     student_id integer,
    #     grade text,
    #     mark integer)""")
    #
    # with conn:
    #     curs.execute(""" CREATE TABLE IF NOT EXISTS employees (
    #     employee_id integer,
    #     name text,
    #     faculty text,
    #     dob TIMESTAMP)""")

    with conn:
        curs.execute(""" CREATE TABLE IF NOT EXISTS degree (
           degree_id integer,
           degree_name text,
           student_id integer,
           student_name text,
           overall_mark integer,
           graduation_year text,
           overall_grade,
           foreign key (student_id) references student (student_id),
           UNIQUE  (degree_id, student_id));
           """)


if __name__ == '__main__':
    create_tables()
