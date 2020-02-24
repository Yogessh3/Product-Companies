string,string_length=input().split(',')
string=list(string)
for i in range(int(string_length)):
    if(string[i]==" "):
        string[i]="%20"
print(*string,sep="")
        
        
