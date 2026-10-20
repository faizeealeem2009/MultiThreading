import threading
import time
sq=[]
cb=[]
def Squares(s,e,a,Name,Version):
    for i in range(s,e):
        # print(a,time.strftime(" %H:%M:%S --"),":",i*i)
        print(a,time.ctime(),":",i*i)
        print(Name,Version,sep="\t")
        sq.append(i*i)
        time.sleep(1)

def cubes(s,e,b,Name,Version,Year):
    for i in range(s,e):
        print(b,time.strftime(" %H:%M:%S --"),":",i*i)
        print(Name,Version,Year,sep="\t")
        cb.append(i*i)
        time.sleep(2)

t1=threading.Thread(target=Squares,args=(1,5,"Square"),kwargs={"Name":"Thread 1","Version":1.5})
t2=threading.Thread(target=cubes,args=(10,15,"Cube"),kwargs={"Name":"Thread 2","Version":2.5,"Year":2025})

t1.start()
t2.start()

t1.join()
t2.join()

print(sq)
print(cb)