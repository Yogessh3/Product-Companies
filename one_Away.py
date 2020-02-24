def distance(string1,string2):
    length_string1=len(string1)
    length_string2=len(string2)
    if(abs(length_string1-length_string2)>1):
        return False
    count=0
    val1=0;val2=0
    while(val1<length_string1 and val2<length_string2):
        if(string1[val1]!=string2[val2]):
            if(count==1):
                return False
            if(length_string1>length_string2):
                val1+=1
            elif(length_string1<length_string2):
                val2+=1
            else:
                val1+=1
                val2+=1
            count+=1
        else:
            val1+=1
            val2+=1
        if(val1<length_string1 or val2<length_string2):
            count+=1
        return count == 1
s1=input()
s2=input()
if distance(s1,s2):
   print("YES")
else:
   print("NO")
