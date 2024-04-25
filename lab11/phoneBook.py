import psycopg2
import csv

DB_NAME = 'postgres'
HS_NAME = 'localhost'
USERNAME = 'postgres'
PWD = '2357'
PT_ID = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host=HS_NAME,
        dbname=DB_NAME,
        user=USERNAME,
        password=PWD,
        port=PT_ID)
    cur = conn.cursor()
    
    create_script = '''CREATE TABLE IF NOT EXISTS phonenumbers (
                         name VARCHAR(255),
                         phonenumber VARCHAR(255))'''
    
    cur.execute(create_script)
    def insert_from_csv(filename):
      with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, phone = row
            cur.execute('''SELECT 1 FROM phonenumbers WHERE name = %s''', (name,))
            
            exists = cur.fetchone()
            if exists:
                cur.execute('''UPDATE phonenumbers
                           SET phonenumber = %s
                           WHERE name = %s''', (name, phone))
            else:
                cur.execute('''INSERT INTO phonenumbers (name, phone) VALUES (%s, %s)''', (name, phone))
            conn.commit()
            
    # insert_from_csv('lab10/data.csv') 
    
    print("if you want to insert user")
    while True:
        user = input("Enter name (0 to exit): ")
        if user == '0':
            break
        number = int(input("Enter phone number: "))
        if number == 0:
            break
        
        cur.execute('''SELECT 1 FROM phonenumbers WHERE name = %s''', (user,))
        exists = cur.fetchone()
        if exists:
            print("The user alredy exists")
        else:
            cur.execute('''INSERT INTO phonenumbers (name, phonenumber)
                           VALUES (%s, %s)''', (user, number))
        conn.commit()
    print("if you want to update user")
    while True:
        user = input("Enter name (0 to exit): ")
        if user == '0':
            break
        number = int(input("Enter phone number: "))
        if number == 0:
            break
        
        cur.execute('''SELECT 1 FROM phonenumbers WHERE name = %s''', (user,))
        exists = cur.fetchone()
        if exists:
            cur.execute('''UPDATE phonenumbers
                           SET phonenumber = %s
                           WHERE name = %s''', (number, user))
        else:
            print("User doesnt exists!")
        conn.commit()
    print("if you want to delete someone enter username: ")
    while True:
        user = input("Enter name (0 to exit): ")
        if user == '0':
            break
        try:
            cur.execute('''DELETE FROM phonenumbers WHERE name = %s''', (user,))
            conn.commit()
            print("Record deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting record:", e)
    cur.execute('''SELECT * FROM phonenumbers''')
    for record in cur.fetchall():
        print(record)
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
