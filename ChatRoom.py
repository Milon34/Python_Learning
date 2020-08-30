import re
s = input()
if re.findall(".*h.*e.*l.*l.*o.*", s):
    print("YES")
else:
    print("NO")

