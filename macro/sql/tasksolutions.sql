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


-- Task 4: Employee Filtering Queries
-- Objective: Filter and categorize employee data.
-- Requirements:
-- ● Find employees with salary between a range
-- ● Search names using LIKE
-- ● Categorize employees using CASE

SELECT * from employee
WHERE salary BETWEEN 60000 and 95000;

SELECT * from employee 
WHERE name LIKE 'k%';

SELECT *,
case 
    when salary>80000 THEN "Grade A"
    when salary >60000 THEN "Grade B"
    Else "Grade C" 
END as Grade
from employee;


-- Task 5: Salary Analysis
-- Objective: Analyze salary data using aggregates.
-- Requirements:
-- ● Find average salary per department
-- ● Show departments with average salary above a threshold

INSERT INTO employee(name,age,department,salary) VALUES('Bhargav',23,'SWE',45624);

SELECT * from employee;
SELECT department , AVG(salary), COUNT(department)
from employee
GROUP BY (department);

SELECT department , AVG(salary) as AVG_SAL
from employee
GROUP BY department
HAVING AVG(salary)>50000;


-- rollup
SELECT department , SUM(salary)
from employee
GROUP BY ROLLUP(department);

-- cube not supported in mysql

-- SELECT department,SUM(salary)
-- from employee
-- GROUP BY CUBE(department);


-- Task 6: Employee & Department Join
-- Objective: Combine data from multiple tables.
-- Requirements:
-- ● Create departments table
-- ● Fetch employee names with department names
-- ● Include employees without department

drop Table employee;
drop table department;


CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);
INSERT INTO department VALUES
(101, 'HR', 'Hyderabad'),
(102, 'IT', 'Bangalore'),
(103, 'Finance', 'Mumbai'),
(104, 'Sales', 'Delhi'),
(105, 'Marketing', 'Chennai');

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

INSERT INTO employee VALUES
(1, 'Rahul', 50000, 102),
(2, 'Priya', 60000, 101),
(3, 'Amit', 55000, 102),
(4, 'Neha', 45000, 103),
(5, 'Vikram', 70000, 104),
(6, 'Sneha', 48000, NULL),
(7, 'Arjun', 52000, 102),
(8, 'Kavya', 65000, NULL);

SELECT employee.emp_name, department.dept_name
from employee
INNER JOIN department
on employee.dept_id=department.dept_id;

SELECT employee.emp_name,department.dept_name
from employee
LEFT JOIN department
on employee.dept_id=department.dept_id;


-- Task 7: Advanced Salary Queries
-- Objective: Use subqueries and CTEs for complex logic.
-- Requirements:
-- ● Find employees earning more than average salary
-- ● Use CTE to rank salaries

SELECT * from employee
WHERE salary>(SELECT AVG(salary) from employee);

with empcte as (
    SELECT * ,
    RANK() OVER(ORDER BY salary DESC)
    from employee
)
SELECT * FROM empcte;


-- Task 8: Query Optimization
-- Objective: Improve query performance.
-- Requirements:
-- ● Create index on salary
-- ● Compare query performance before and after index

SELECT * from employee;

EXPLAIN
SELECT * from employee
WHERE emp_name='Neha';
-- -> Filter: (employee.emp_name = 'Neha')  (cost=1.05 rows=1)
--     -> Table scan on employee  (cost=1.05 rows=8)

CREATE INDEX name_index
on employee(emp_name);

EXPLAIN
SELECT * from employee
WHERE emp_name='Neha';

-- -> Index lookup on employee using name_index (emp_name = 'Neha')  (cost=0.35 rows=1)






