import pymysql
# =========================================================connecting db
my_db=pymysql.connect(user="root", password="darling.in",host="localhost",database="10kc")
print("connected")
cur=my_db.cursor()




# =======================================================inserting data to db tables
# num=int(input("Enter roll num:"))
# name=input("Enter your name:")
# query="insert into student values(%s,%s)"
# cur.execute(query,(num,name))
# my_db.commit()
# print("inserted successfully")
# cur.close()



# =============================================fetching data from db
# query=("select * from student")
# cur.execute(query)
# rows=cur.fetchall()
# # print(rows)
# for row in rows:
#     print(row)






