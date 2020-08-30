'''
x=["java","python","R","C#"]
x.append("C")
x.append("C++")
print(x)
print(x.pop())
print(x)
print(x.pop())
print(x)
'''
'''
import queue
L=queue.Queue(maxsize=10)
L.put(9)
L.put(6)
L.put(5)
L.put(4)
print(L.get())
print(L.get())
print(L.get())
print(L.get())
'''
'''
from tkinter import *
top=Tk()
top.mainloop()
'''
'''
from time import *
from  datetime import *
host_path=r"/etc/hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","https://www.facebook.com"]
while True:
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,17):
        print("working hours")
        with open(host_path,"r+") as fileptr:
            content=fileptr.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    fileptr.write(redirect+" " +website+"\n")
    else:
        print("Fun hours")
        sleep(5)
'''
'''
import json
print(dir(json))
'''
'''
import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))


b=np.array([[1,2],[3,2],[6,3]])
print("printing the elments..")
print(b)
b=b.reshape(2,3)
print("printing the reshape array..")
print(b)
'''
import  numpy as np
a=np.array([[1,2],[3,4],[8,1]])
print(a[0,1])
print(a[2,0])
y=[]
for x in range(0,9,2):
    a=y.append(x)
    print(a)