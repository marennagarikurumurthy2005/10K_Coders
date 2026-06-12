-- ● Create an employees table
-- ● Columns: emp_id, name, age, department, salary
-- ● emp_id must be primary key
-- ● salary cannot be NULL

show TABLEs;

CREATE table employee(emp_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200),age INT,department VARCHAR(200),salary DECIMAL(10,2) NOT NULL);

INSERT into employee(name,age,department,salary) VALUES
('Ganesh',31,'sales',00000);


SELECT * from employee;


DESC employee;