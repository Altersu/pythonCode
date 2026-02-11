


from  pymysql  import Connection

conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    autocommit = True
)

# print(conn.get_server_info())
cursor = conn.cursor()
conn.select_db("test")
# cursor.execute("create table test_pymysql(id int,name varchar(20));")
# cursor.execute("select * from student")
cursor.execute("insert into test_pymysql values(2,'xiaomei');")
# conn.commit()
# results = cursor.fetchall()
# for r in results:
#     print(r)
conn.close()