import pymysql
my_db=pymysql.connect(user="root", password="darling.in",host="localhost",database="10kc")
print("connected")
cur=my_db.cursor()
query="select * from det"
cur.execute(query)
cur.close()
