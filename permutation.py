def check(str1,str2):
    no_of_chars=256
    ct_arr1=[0]*256
    ct_arr2=[0]*256
    length_str1=len(str1)
    length_str2=len(str2)
    for i in str1:
        ct_arr1[ord(i)]=1
    for i in str2:
        ct_arr2[ord(i)]=1
    if(length_str1!=length_str2):
        return False
    else:
        for i in range(no_of_chars):
            if(ct_arr1[i]!=ct_arr2[i]):
                return False
        return True
str1=input()
str2=input()
if(check(str1,str2)):
    print("Yes")
else:
    print("No")

