n=int(input())
a = [int(s) for s in input().split(' ')]
increment=1
max_increment=1
for i in range(1,n):
    if a[i]>a[i-1]:
        increment=increment+1
    else:
        max_increment=max(max_increment,increment)
        increment=1
max_increment=max(max_increment,increment)
print(max_increment)