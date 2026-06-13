-- ● Create an employees table
-- ● Columns: emp_id, name, age, department, salary
-- ● emp_id must be primary key
-- ● salary cannot be NULL

show TABLEs;

CREATE table employee(emp_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200),age INT,department VARCHAR(200),salary DECIMAL(10,2) NOT NULL);

INSERT into employee(name,age,salary) VALUES
('Ganesh',31,00000);

SELECT * from employee;

DESC employee;

-- Task 2: Table Modification
-- Objective: Modify an existing table using DDL commands.
-- Requirements:
-- ● Add email column with UNIQUE constraint
-- ● Add default value to department
-- ● Drop an unused column

alter Table employee
add COLUMN email VARCHAR(50) UNIQUE;

ALTER Table employee
MODIFY  department VARCHAR(200) DEFAULT 'ninja';

UPDATE employee
SET email="murthy@gmail.com" where emp_id=1;

DELETE FROM employee
WHERE emp_id=8 or emp_id=7;

ALTER Table employee
DROP COLUMN age;

-- ask 3: Employee Data Management
-- Objective: Perform data manipulation operations.
-- Requirements:
-- ● Insert at least 10 employee records
-- ● Update salary of a department
-- ● Delete employees with NULL department

drop Table employee;

CREATE table employee(emp_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200),age INT,department VARCHAR(200),salary DECIMAL(10,2) NOT NULL);

INSERT into employee(name,age,department,salary)
VALUES
("kurumurthy",21,'SWE',70000),
("Devratha",51,'Sales',60000),
("Vardha",51,'admini',62000),
("Pandith",29,'SWE',70000),
("Bilal",41,'support',40000);

INSERT INTO employee(name,age,salary)
VALUES
('dileep',40,45624),
('sandeep',30,45624),
('sunil',41,45624),
('vishal',43,45624),
('sreenu',30,45624);

SELECT * from employee;

UPDATE employee
set salary=85000 WHERE department="swe";

DELETE  FROM employee
WHERE department is NULL;


