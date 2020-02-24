string=input()
compressed_string=[]
curr_count=0
for i in range(len(string)-1):
    if(string[i]==string[i+1]):
        curr_count+=1
    else:
        curr_count+=1
        val=[string[i],curr_count]
        compressed_string.extend(val)
        curr_count=0
if(string[-1]!=string[-2]):
    compressed_string.append(string[-1])
    compressed_string.append(curr_count+1)
else:
    compressed_string.append(string[i])
    compressed_string.append(curr_count+1)
print(*compressed_string,sep="")
        
