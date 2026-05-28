
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
INSERT into students VALUES(3,"murthy",23,'2003-03-09');


UPDATE students
set name="devratha"
WHERE id=2;

DELETE FROM students
WHERE id=1;

SELECT * from students;


-- DQL : select and select all

SELECT name , age 
from students;

--  to select unique records we use distinct

SELECT  DISTINCT name from students;

SELECT DISTINCT * from students;

-- TCL commands

TRUNCATE TABLE students;

SAVEPOINT s1;


set autocommit=0;
INSERT into students(id,name,age,dob)VALUES
    (1,'Murthy',21,'2005-03-09'),
    (2,'Devratha',40,'1990-03-08'),
    (3,'Vardha',39,'1990-09-07');

SAVEPOINT s2;

SELECT * FROM students;

DELETE FROM students
WHERE id=2;
SAVEPOINT s3;

-- TRUNCATE Table students;

-- SAVEPOINT s4;

ROLLBACK TO s2;

COMMIT;


-- DCL Commands Grant and revoke

GRANT SELECT,UPDATE on students to murthy;

REVOKE SELECT,UPDATE on students from murthy;