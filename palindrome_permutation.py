str1=input()
pal_str=[]
odd_ct=0
even_ct=0
temp_str=[]
for i in range(len(str1)):
    if(str1.count(str1[i])%2==0 and str1[i] not in temp_str):
        even_ct+=str1.count(str1[i])
    else:
        odd_ct+=str1.count(str1[i])
    temp_str.append(str1[i])
if(abs(odd_ct-even_ct)==1 or abs(odd_ct-even_ct)==0):
   print("Yes")
else:
   print("No")

        
