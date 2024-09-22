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
 cur.execute('DROP TABLE IF EXISTS users')
 create_script =  '''CREATE TABLE IF NOT EXISTS users (
                      id serial PRIMARY KEY,
                      name VARCHAR(60),
                      MATH_1 INTEGER,                 
                      BEE INTEGER,
                      MECHANICS INTEGER,
                      PHY INTEGER,
                      CHEM INTEGER,
                      IA_MATH_1 INTEGER,
                      IA_BEE INTEGER,
                      IA_MECHANICS INTEGER,
                      IA_PHY INTEGER,
                      IA_CHEM INTEGER
                      );'''
 cur.execute(create_script)
 conn.commit()
 print("Table created successfully\n") 

 #inserting one and many values into table
 inster_script = 'INSERT INTO users (id ,name, MATH_1,BEE,MECHANICS,PHY,CHEM,IA_MATH_1,IA_BEE,IA_MECHANICS,IA_PHY,IA_CHEM)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
 insert_value = [(1,'Madan',90,89,78,67,92,16,7,20,18,1),(2,'Arun',58,39,59,90,22,16,7,20,18,1),(3,'NOOB',92,21,21,34,43,16,7,20,18,1),(4,'AdrARSH',43,53,22,44,11,16,7,20,18,1),(5,'SUGANTHI',1,1,1,1,1,1,1,1,1,1),(6,'MUTURAJ',90,90,90,90,90,20,20,20,20,20,)]
 for record in insert_value: #record will have every value once in the loop
  cur.execute(inster_script,record)

 print("INSERTED VALUES SUCCESFULLY\n")

 print("THE STUDENTS WHOS MARKS ARE GREATER THEN 90 IN THE SUBJECT MATH_1 ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE MATH_1 >= 90;") #math1>90 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE GREATER THEN 90 IN THE SUBJECT BEE ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE BEE >= 90;") #BEE>90 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name) 

 print("THE STUDENTS WHOS MARKS ARE GREATER THEN 90 IN THE SUBJECT MECHANICS ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE MECHANICS >= 90;") #mechanics>=90 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name) 

 print("THE STUDENTS WHOS MARKS ARE GREATER THEN 90 IN THE SUBJECT PHY ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE PHY >= 90;") #phy>=90 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE GREATER THEN 90 IN THE SUBJECT CHEM ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE CHEM >= 90;") #chem>=90 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 32 IN THE SUBJECT MATH_1 ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE MATH_1 <= 32;") #Math_1<=32 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 32 IN THE SUBJECT BEE ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE BEE <= 32;") #BEE<=32 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 32 IN THE SUBJECT MECHANICS ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE MECHANICS <= 32;") #mechanics<=32 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)


 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 32 IN THE SUBJECT CHEM ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE CHEM <= 32;") #Chem<=32 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)


 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 32 IN THE SUBJECT PHY ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE PHY <= 32;") #phy<=32 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR GREATER THEN 16 IN THE SUBJECT IA_MATH_1 ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_MATH_1>=16;") #IA_MATH_1>=16 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR GREATER THEN 16 IN THE SUBJECT IA_BEE ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_BEE>=16;") #IA_BEE>=16 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR GREATER THEN 16 IN THE SUBJECT IA_MECHANICS ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_MECHANICS>=16;") #IA_MECHANICS>=16 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR GREATER THEN 16 IN THE SUBJECT IA_PHY ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_PHY>=16;") #IA_PHY>=16 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR GREATER THEN 16 IN THE SUBJECT IA_CHEM ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_CHEM>=16;") #IA_CHEM>=16 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 8 IN THE SUBJECT IA_MATH_1 ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_MATH_1<= 8;") #IA_MATH_1<=8 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)


 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 8 IN THE SUBJECT IA_BEE ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_BEE<= 8;") #IA_BEE<=8 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)  

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 8 IN THE SUBJECT IA_MECHANICS ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_MECHANICS<= 8;") #IA_MECHANICS<=8 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)  

 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 8 IN THE SUBJECT IA_PHY ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_PHY<= 8;") #IA_PHY<=8 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name)  


 print("THE STUDENTS WHOS MARKS ARE EQUAL OR LESS THEN 8 IN THE SUBJECT IA_CHEM ARE:\n")
 cur.execute("SELECT id,name FROM users WHERE IA_CHEM<= 8;") #IA_CHEM<=8 condition
 high_marks_names = cur.fetchall()
 for name in high_marks_names:
    print(name) 

except Exception as error:
 print(error)
finally:
 if cur is not None:
  cur.close()  
