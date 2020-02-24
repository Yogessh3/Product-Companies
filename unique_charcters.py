string=input()
string_copy=[]
flag=0
for i in string:
    if i not in string_copy:
        string_copy.append(i)
    else:
        flag=1
        break
if(flag==0):
    print('YES The String has Unique Characters')
else:
    print('NO The String has repeated Characters')
