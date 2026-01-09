show databases;
show TABLES;

CREATE table marks(Number INT,marks INT);

INSERT into marks VALUES(724,80),
(731,85),
(757,60),
(740,98);
SELECT * from student;
SELECT *from marks

--  innerjoin
SELECT * from student INNER JOIN marks on student.`Number`=marks.`Number`;

SELECT * from student CROSS JOIN marks on student.`Number`=marks.`Number`;

SELECT * from student LEFT JOIN marks on student.`Number`=marks.`Number`;

SELECT * from student RIGHT JOIN marks on student.`Number`=marks.`Number`;


SELECT * from student JOIN marks on student.`Number`=marks.`Number`;

SELECT * from student JOIN marks on student.`Number`=marks.`Number`;

# union , union all is used when want to join left and right join


DELIMITER $$
CREATE Trigger t1
AFTER INSERT on student
for EACH ROW
begin
INSERT into marks(`Number`) VALUES(NEW.NUMBER);
END$$
DELIMITER;

INSERT into student VALUES(780,"Murthy");

SELECT * from marks;



--  for normal from CREATE Table sports(sport_id INT,sport_name VARCHAR(30),fav_player varchar(30),specs VARCHAR(30),country VARCHAR(30));