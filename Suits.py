a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
Mnf=0
Mns=0
Mnf=min(a,d)
Mns=min(b,c)
if (d > Mns):
    Mns=abs(Mns-d)
    d=abs(Mns-d)
    Mns=e*Mns
    d=f*d
    print(Mns+d)
else:
    print(Mnf*f)

