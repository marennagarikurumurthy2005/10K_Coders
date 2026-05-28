
--  DDL commands
create DATABASE inter;
show DATABASES;
use inter;
-- creation
create Table students(
    id INT,
    name VARCHAR(50),
    age INT,
    dob DATE
);
DESC student;
ALTER Table student
add city VARCHAR(20);
ALTER Table student MODIFY city CHAR(50);
ALTER Table student drop COLUMN city;
RENAME TABLE student TO students;
SELECT * FROM students;
INSERT into students(id,name,age,dob)values(
    1,"murthy",20,'2005-03-09'
);
TRUNCATE Table students;
drop Table students;


-- DML commands

INSERT into students VALUES(2,"deva",23,'2003-03-09');

UPDATE students
set name="devratha"
WHERE id=2;

DELETE FROM students
WHERE id=1;

SELECT * from students;


-- DQL : select and select all
