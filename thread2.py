import time
import threading

def Display():
    l1=[1,2,3,4,5,6,7,8,9,0]
    for i in l1:
        print("Display",i)
        time.sleep(3)

def Sum():
    l1=[1,2,3,5,8,6,4,9,7]
    s=0
    for i in l1:
        s+=i
        print("Sum",s)
        time.sleep(3)

def String():
    stri="PythonThread"
    s=[]
    for i in stri:
        s.append(i)
        print("String",s)
        time.sleep(3)

t1=threading.Thread(target=Display)
t2=threading.Thread(target=Sum)
t3=threading.Thread(target=String)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()