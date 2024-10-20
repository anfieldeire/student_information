

CREATE_STUDENT = "INSERT into STUDENT (name, home_address, dob) VALUES (?,?,?)"

GET_STUDENT = "SELECT * from STUDENT WHERE student_id = (?);"

UPDATE_STUDENT = "UPDATE STUDENT set name=(?), home_address=(?) WHERE student_id = (?)"

CREATE_COURSE = "INSERT into COURSES (name) VALUES (?)"

UPDATE_COURSE = "UPDATE COURSES set name=(?) WHERE course_id=(?)"

CREATE_MARK = "INSERT into MARKS (course_id, course_name, student_id, student_name, mark, year) VALUES (?,?,?,?,?,?)"

GET_MARKS = "SELECT course_name, mark from MARKS WHERE course_id = (?) AND student_id = (?)"
