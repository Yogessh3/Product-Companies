row,column=map(int,input().split())
mat=[]
for i in range(row):
    l=[int(x) for x in input().split()]
    mat.append(l)
r=[]
c=[]
for i in range(row):
    for j in range(column):
        if(mat[i][j]==0):
            r.append(i)
            c.append(j)
for i in range(row):
    for j in range(column):
        if(i in r or j in c):
            mat[i][j]=0
for i in mat:
    print(*i)
        
        
