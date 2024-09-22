import  psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
password = '123'
port = 5432
conn = None
cur = None

# Connect to the database server.
try: 
 conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = password,
    port = port
)
 #creating a table 
 cur = conn.cursor()
 cur.execute('DROP TABLE IF EXISTS first')
 create_script =  '''CREATE TABLE IF NOT EXISTS first (
                      id serial PRIMARY KEY,
                      name VARCHAR(60),
                      email VARCHAR(80),                 
                      phone VARCHAR(15)
                      );'''
 cur.execute(create_script)

#inserting one and many values into table
 inster_script = 'INSERT INTO first (id ,name,email,phone)VALUES(%s,%s,%s,%s)'
 insert_value = [(1,'Madan',12000,'A1'),(2,'prem',13000,'A2'),(3,'bushan',14000,'A3'),(4,'kunal',15000,'A4')]
 for record in insert_value: #record will have every value once in the loop
  cur.execute(inster_script,record)

 print("TABLE CREATED")  


 #update_script = 'UPDATE first SET email = email + 10000'
 #cur.execute(update_script)

 #delete_script = 'DELETE FROM first WHERE name = %s'
# delete_record = ('Madan')
# cur.execute(delete_script,(delete_record))
 #cur.execute("SELECT name FROM first WHERE marks > 90;")
 #high_marks_names = cur.fetchall()
 #print("\nNames with marks more than 90:")
 #for name in high_marks_names:
   # print(name)

 #display the records as we want  
 #cur.execute('SELECT*FROM first')
 #for record in cur.fetchall():
        #print(record['id'], record['name'])


 conn.commit() 
except Exception as error:
 print(error)
finally:
 if cur is not None:
  cur.close()  
