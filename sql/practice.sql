
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

use inter;

SELECT * from student
WHERE id in (SELECT id from dept 
where(department='CSE'));

-- exist
SELECT * 
from student
where EXISTS(SELECT *
from dept
where student.id=dept.id);

SELECT * from student;

SELECT MAX(fee) from student; --70000

SELECT MIN(fee) from student; --45000

SELECT AVG(fee) from student; --53000

SELECT * from student
WHERE fee in (70000,45000);

use inter;

SELECT * from student;

SELECT name from student
WHERE name LIKE 'M%';


--  creating view

CREATE View student_view AS
SELECT name,fee from student;

SELECT * from student_view;

use inter;

DROP VIEW student_view;


CREATE INDEX student_index
on student(id);

SELECT * from student
WHERE(name='Murthy');


CREATE Procedure fetchDetails()
begin

SELECT * from student
WHERE(fee>48000);

END;

CALL fetchDetails();


create Procedure left_Join()
BEGIN

SELECT * FROM student
LEFT JOIN dept
on student.id=dept.id;

END;

call left_Join();

use inter;

-- CREATE Procedure inner_Join()
-- begin

-- SELECT  id, name,fee,department from student 
-- INNER JOIN dept
-- on student.id=dept.id;

-- END;
DROP Procedure inner_Join;

CREATE Procedure inner_Join()
begin

SELECT  student.id, name,fee,department from student 
INNER JOIN dept
on student.id=dept.id;

END;

CALL inner_Join();

use inter;

use 10kc;
DROP TABLE cartItems;

DROP TABLE addtocart;


CREATE TABLE addtoCart(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(500)
);

CREATE TABLE cartItems(
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    cart_id INT,
    name VARCHAR(500),
    FOREIGN KEY (cart_id) REFERENCES addtoCart(id)
);




-- CREATE table addtoCart(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(500));
-- create Table cartItems(id INT AUTO_INCREMENT, FOREIGN key(id) REFERENCES addtoCart(id),name VARCHAR(500));



-- triggers



CREATE Trigger cartTrigger
AFTER INSERT on addtoCart
for each ROW
BEGIN
INSERT INTO cartItems(cart_id,name)
VALUES(NEW.id,NEW.name);
END;

INSERT INTO addtoCart(name)
VALUES('laptop'),
('mobile'),
('fridge');

SELECT * FROM addtoCart;

SELECT * FROM cartItems;

CREATE Trigger delTrigger
BEFORE DELETE on cartItems
for EACH ROW
begin

DELETE from addtoCart
WHERE id=OLD.id;


END;

DELETE from addtoCart
WHERE(id=3);

drop TABLE nirven;
use 10kc;


use inter;
TRUNCATE Table nirven;

DROP Trigger pop_trigger;

CREATE table nirven(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(200), num INT);



CREATE Table kothakota(village_id INT AUTO_INCREMENT PRIMARY key , fam_id INT, num INT );


CREATE Trigger pop_trigger
AFTER INSERT on nirven
for each row 
BEGIN

INSERT INTO kothakota(fam_id,num) 
VALUES(NEW.id,NEW.num);



END;







INSERT INTO nirven(name, num)
VALUES
    ('Murthy', 101),
    ('Ravi', 102),
    ('Kiran', 103),
    ('Vardha', 104),
    ('Devratha', 105);


INSERT INTO nirven(name, num)
VALUES
    ('Suresh', 106),
    ('Mahesh', 107),
    ('Ajay', 108),
    ('Ramesh', 109),
    ('Praveen', 110);

SELECT * from nirven;

SELECT * from kothakota;

TRUNCATE Table kothakota;



SELECT village_id,fam_id,name,nirven.num 
from nirven inner JOIN kothakota
on nirven.id=kothakota.fam_id;

CREATE table sbi(id int PRIMARY key AUTO_INCREMENT,name VARCHAR(200),balance INT);

INSERT INTO sbi(name, balance)
VALUES
    ('Murthy', 50000),
    ('Ravi', 35000),
    ('Kiran', 75000),
    ('Vardha', 42000),
    ('Devratha', 100000);



--  transactions in sql
set autocommit=0;

SELECT * FROM sbi;

DELIMITER//

START TRANSACTION//
UPDATE sbi
set balance=balance-100
WHERE id=1//
UPDATE sbi
set balance=balance+100
WHERE id=5//
COMMIT//


DELIMITER;

use inter;

SHOW TABLEs;



SELECT * from sbi;

-- second heighest salary
SELECT MAX(balance) 
from sbi 
where balance<(SELECT max(balance)
from sbi);


SELECT DISTINCT balance
from sbi
ORDER BY balance DESC
LIMIT 1 OFFSET 4;


SELECT name,count(*)
from sbi
GROUP BY name 
HAVING COUNT(*)>1;


-- DELETE from sbi
-- where id not in (
--     SELECT min(id)
--     from sbi
--     GROUP BY name
-- );

use inter;

DELETE from sbi
where id not in (
SELECT id from (
    SELECT MIN(id) as id
    from sbi
    GROUP BY name
) as temp
);





























