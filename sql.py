

CREATE_STUDENT = "INSERT into STUDENT (name, home_address, dob) VALUES (?,?,?)"

GET_STUDENT = "SELECT * from STUDENT WHERE student_id = (?);"

UPDATE_STUDENT = "UPDATE STUDENT set name=(?), home_address=(?) WHERE student_id = (?)"

CREATE_COURSE = "INSERT into COURSES (name, course_id) VALUES (?, ?)"
