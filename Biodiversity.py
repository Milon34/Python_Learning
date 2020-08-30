import re
a=int(input())
for i in range (0,a):
   s = input()

   if re.findall(s, s):
    print(s)
   else:
     print("NONE")