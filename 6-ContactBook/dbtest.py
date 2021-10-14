import apsw

# Opening/creating database
connection=apsw.Connection("testdb")
cursor=connection.cursor()

# simple statement
cursor.execute("create table if not exists inventory(id,product,price,quantity)")

# Basic table inserts
#cursor.execute("insert into inventoRY values(2,'Apple',0.60,45);")
#cursor.execute("insert into inventoRY values(3,'Pineapple',7.00,13);")
#cursor.execute("insert into inventoRY values(4,'Kiwi',0.55,16);")



cursor2=connection.cursor()

# This is the preferred way for obtaining all of the results from a query
rows = list( cursor2.execute("select * from inventory") )

for row in rows:
    print(row)
