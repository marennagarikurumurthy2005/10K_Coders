import pymysql
my_db=pymysql.connect(host="localhost",user='root',password="darling.in" ,database="studentdb")
curse=my_db.cursor()
curse.execute("create database if not exists studentdb")
my_db.commit()
print("DB created successfully")


query="create table if not exists students (id int primary key, name varchar(200),branch varchar(200),year int)"
curse.execute(query)
my_db.commit()
print("table created")


# # qi="insert into students values(724,'Murthy','csd',4)"
# qi="insert into students values(700,'navneetha','csd',4)"
# curse.execute(qi)
# my_db.commit()

def insert(id,name,branch,year):
    # fetchq="select * from students"
    # curse.execute(fetchq)
    # data=curse.fetchall()
    # for i in data:
    #     if id==i[0]:
    #         print("student already exist")

    try:
        query="insert into students (id,name,branch,year)values(%s,%s,%s,%s)"
        curse.execute(query,(id,name,branch,year))
        my_db.commit()
    except:
        print("Student already exist with this id")

def update(id,name,branch,year):
    try:
        # if "name" in kwargs:
        #     name=kwargs['name'] 
        # if "branch" in kwargs:
        #     branch=kwargs['branch']
        # if "year" in kwargs:
        #     year=kwargs['year']
        query="update students set name=%s,branch=%s,year=%s where id=%s"
        curse.execute(query,(name,branch,year,id))
        my_db.commit()
        print("Update success")
    except:
        print("Id not found")

update(id=724,name="Kurumurthy",branch="csd",year=2)





# insert(725,"laxman","csd",4)
fetchq="select * from students"
curse.execute(fetchq)
data=curse.fetchall()
print(data)



# for i in data:
#     print(i[0])








