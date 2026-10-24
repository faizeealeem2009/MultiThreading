import threading
import os
import time
import numpy as np
import mysql.connector

def store_numpy():
    os.chdir("D:\\contents")
    with open("data.csv","r") as f1:
        data=np.array(f1.read().split(","),dtype=(str))
        print(data)
        f1.close()
    time.sleep(2)

    with open("log.txt","w") as f2:
        f2.write(time.strftime("%H:%M:%S")+ "\n")
        f2.close()

def read_from_txt():
    os.chdir("D:\\contents")
    with open("read_data.txt","r") as f1:
        data=f1.read()
        change_case=data.swapcase()
        print(change_case)
        f1.close()
    os.chdir("D:\\Faizee Abdul Aleem Python\\Python Projects\\MULTITHREADING")
    with open("new_read_data.txt","w")as f1:
        f1.write(change_case)
        f1.close()
    time.sleep(3)

    with open("log.txt","a") as f2:
        f2.write(time.strftime("%H:%M:%S")+ "\n")
        f2.close()
    

def mysql_read_data():
    try:
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="bismillah",
        database="school"
        )
    except:
        print("Unable to connect the database")
    else:
        print("Connection Established")
        mycursor=conn.cursor()
        mycursor.execute("SELECT * FROM students")
        records=mycursor.fetchall()

        for r in records:
            print(r)

        mycursor.close()
        conn.close()
    time.sleep(4)
    
    with open("log.txt","a") as f2:
        f2.write(time.strftime("%H:%M:%S"))
        f2.close()

t1=threading.Thread(target=store_numpy)
t2=threading.Thread(target=read_from_txt)
t3=threading.Thread(target=mysql_read_data)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()