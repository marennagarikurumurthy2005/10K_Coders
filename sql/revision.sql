-- DDL commands create,alter,drop,truncate,rename for table archi-tecture
show DATABASES;
use 10kc;
show TABLEs;
create table hostel(num int,name varchar(10),fee int,food_rating varchar(10));
ALTER TABLE hostel RENAME COLUMN num to Number;
DESC hostel;
ALTER Table hostel RENAME to hostels;
ALTER Table hostels RENAME to hostel;

SELECT * from hostel;
TRUNCATE Table hostel;

DROP Table hostel;


DESC hostel;
insert into hostel values(01,"RRBH",5000,"good"),
(02,"KRBH",5500,"bad");


-- establishing relation or connection with primary and forein keys
create table fam(id int PRIMARY KEY,size int);
CREATE table det(id int, FOREIGN KEY (id) REFERENCES fam(id), head varchar(40));
INSERT into det VALUES(01,"A");

INSERT INTO fam VALUES(01,5);




-- DML COMMANDS  insert,update , delete, 

create table hostel(num int PRIMARY KEY,name varchar(10),fee int,food_rating varchar(10));
insert into hostel values(01,"RRBH",5000,"good"),
(02,"KRBH",5500,"bad");

UPDATE hostel fee set fee=2000 WHERE fee=5000;

UPDATE hostel set fee=5000 WHERE name="RRBH";

DELETE from hostel WHERE num=02;

SELECT * from hostel;


-- DQL select, from used to visualize

SELECT * FROM hostel;


-- clauses where , distinct , groupby , orderby , like, between,limit/offset,having,in

SELECT * from rrbh;
SELECT * from rrbh WHERE amount=5000;

SELECT * from rrbh WHERE amount>5000;

SELECT DISTINCT amount from rrbh;

SELECT amount,COUNT(amount)
from rrbh
GROUP BY amount;

SELECT * from rrbh;

SELECT receipt_taken,COUNT(receipt_taken)
from rrbh
GROUP BY(receipt_taken);

INSERT into rrbh VALUES(now(),5,"GK",4500,0);



SELECT * from rrbh ORDER BY(receipt_taken);
SELECT * from rrbh where `Name` Like '%k';

SELECT * from rrbh where amount BETWEEN 5000 and 6000;

SELECT * from rrbh LIMIT 1 OFFSET 2;

SELECT * from rrbh;


SELECT Name, AVG(amount)
from rrbh
GROUP BY Name
HAVING AVG(amount)>5000;

SELECT * from rrbh; 

SELECT * from rrbh WHERE Name in ("MK","RK"); 














