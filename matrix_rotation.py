row,column=map(int,input().split())
mat=[]
for i in range(row):
    l=[int(x) for x in input().split()]
    mat.append(l)
answer_mat=[]
curr_row=row-1
for i in range(column):
    l=[]
    curr_row=row-1
    for j in range(row):
        l.append(mat[curr_row][i])
        curr_row-=1
    answer_mat.append(l)
for i in answer_mat:
    print(*i)
        
        
