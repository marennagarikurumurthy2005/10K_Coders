use 10kc;
show TABLES;

CREATE Table student(Number INT,Name VARCHAR(30));

DESC student;


-- method 1
INSERT into student(`Number`,`Name`)
VALUES(724,"Kurumurthy");

SELECT * from student;

-- method 2
INSERT into student(`Number`,`Name`)
VALUES
(731,"Yaseen"),
(757,"Vamc");

SELECT * from student;

-- method 3 
INSERT into student VALUES
(728,"madhu"),
(704,"anil");


SELECT * from student

CREATE table RRBH(fee_paid DATETIME DEFAULT CURRENT_TIMESTAMP, id VARCHAR(13), Name VARCHAR(30),amount FLOAT , receipt_taken BOOLEAN DEFAULT False);

desc rrbh;

INSERT INTO rrbh(`id`,`Name`,`amount`)
VALUES
(1,"MK",5000.00),
(2,"RK",6000.00);

SELECT * from rrbh;
INSERT INTO rrbh (`id`,`Name`,`amount`,`receipt_taken`)
VALUES
(3,"VK",6000.00,TRUE);

SELECT * from rrbh;



 