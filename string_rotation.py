s1=input()
s2=input()
def check_rotation(str1,str2):
    first_letter=str2[0]
    ind=0
    for i in range(len(str1)):
        if(str1[i]==first_letter):
            ind=i
            break
    ans=str1[ind:]+str1[:ind]
    if(ans==str2):
        return True
    else:
        return False
if check_rotation(s1,s2):
    print("Yes")
else:
    print("No")
        
        
        
        
    
