
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


CREATE table murthy(id INT PRIMARY KEY,name VARCHAR(50));

CREATE Table mk(id INT, Foreign Key (id) REFERENCES murthy(id),name VARCHAR(50));

INSERT INTO murthy VALUES(2,'murthy',25);
INSERT INTO mk VALUES(1,'Kurumurthy');

SELECT * from murthy;

ALTER Table murthy
ADD COLUMN age INT CHECK(age>=18) DEFAULT 18;

SELECT * FROM mk;

DROP Table murthy;

DROP Table mk;

SELECT COUNT(*) FROM murthy;

show tables;

use inter;

show TABLES;

create table student(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),fee INT);

INSERT INTO student(name, fee)
VALUES
    ('Manikanta', 50000),
    ('Manohar', 45000);
    -- ('Kiran', 60000),
    -- ('Vardha', 55000),
    -- ('Devratha', 70000);

SELECT * from student;

CREATE Table dept(id INT , FOREIGN Key(id) REFERENCES student(id),department VARCHAR(50));

INSERT INTO dept(id, department)
VALUES
    (1, 'CSE'),
    (2, 'ECE'),
    (3, 'AI & DS'),
    (4, 'MECH'),
    (5, 'CIVIL');

SELECT * FROM dept;

TRUNCATE Table dept;


-- inner join

SELECT * from student
INNER JOIN dept 
on student.id=dept.id;


SELECT * from student 
LEFT JOIN dept
on student.id=dept.id;

SELECT * from dept;
SELECT* from student;

SELECT * FROM student
RIGHT JOIN dept
ON student.id=dept.id;



--  it does nit works in mysql alternatively union left and right joins 
-- SELECT * FROM student 
-- FULL OUTER JOIN dept
-- on student.id=dept.id;
use inter;

SELECT * FROM student
LEFT JOIN dept
on student.id=dept.id
UNION
SELECT * FROM student
RIGHT JOIN dept
on student.id=dept.id;

SELECT * FROM student as s
JOIN student 
on s.id=student.id;

SELECT * FROM student
CROSS JOIN dept;


-- sub queries 















