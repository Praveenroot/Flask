import sqlite3
con=sqlite3.connect("C:\\Users\\Praveen Kumar\\Downloads\\Flask-Projects-master\\contact_project\\contact.db")
cursor=con.cursor()
cursor.execute("""create table dbservice(ip varchar, http varchar, time varchar, count integer, Sno integer primary key autoincrement);""")
con.commit()
con.close()

print("Table Created Successfully")