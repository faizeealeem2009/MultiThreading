import threading
import time
import os

def file_read_write(file1,file2):
    os.chdir("D:\\contents")
    mydata=""
    with open(file1,"r") as f1:
        mydata=f1.read()
        f1.close()

    os.chdir("D:\\Faizee Abdul Aleem Python\\Python Projects\\MULTITHREADING")
    with open(file2,"w") as f2:
        f2.write(mydata)
        f2.close()
        time.sleep(2)

    print(time.strftime("%H:%M:%S"))


def file_read_write2(file1,file2):
    os.chdir("D:\\contents")
    mydata=""
    with open(file1,"r") as f1:
        mydata=f1.read()
        f1.close()

    os.chdir("D:\\Faizee Abdul Aleem Python\\Python Projects\\MULTITHREADING")
    with open(file2,"w") as f2:
        f2.write(mydata)
        f2.close()
        time.sleep(2)

    print(time.strftime("%H:%M:%S"))


t1=threading.Thread(target=file_read_write,args=("employees.txt","new_employees.txt"))
t2=threading.Thread(target=file_read_write2,args=("emp2.txt","new_employees2.txt"))


t1.start()
t2.start()
t1.join()
t2.join()