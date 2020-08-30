'''
import pandas as pd
import numpy as np
info = np.array(['P','a','n','d','a','s'])
a = pd.Series(info)
print(a)
import pandas as pd
# a list of strings
x = ['Python', 'Pandas']
# Calling DataFrame constructor on list
df = pd.DataFrame(x)
print(df)
'''
'''
def intro():
    print("milon")
intro()
'''
'''
for i in range(5):
    print(i)
    if(i==3):
        break
'''
'''
n = input("Enter a number: ")

factorial = 1
if int(n) >= 1:
    for i in range (1,int(n)+1):
        factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)
'''
'''
n = int(input("Enter a number: "))
fact=1
for i in range(1,int (n)+1):
    if n>0:
        fact=fact*i
    elif n==0:
        print("N/A")
    else:
        print("1")


print("the number",n,"is", fact)
'''
'''
tup1="Hello"
print(type(tup1))
tup2="java",
print(type(tup2))
'''
'''
tuple1=tuple(input("Enter the tuple elements:"))
count=0
print(tuple1)
for i in  tuple1:
    print("tuple1[%d]=%s"%(count,i))
    count=count+1
 '''
'''
#tuple1=(1,2,3,4,5)
#print(tuple1)
#del tuple1[0]
#a=[7,4,5,7,7]
#b=a
#a[3]='milon'
#print(a)
'''
#milon=()
#print(milon.__sizeof__())
#abc=set(["january","february"])
#abc.update(["March"])
#print(abc)
#r=set(input("Enter set:"))
#r.discard(2)
#print(r)
months ={1,2,3,4,5,2}
months.remove(1);
months.remove(2);
print(months)
for i in months:
    print(i)