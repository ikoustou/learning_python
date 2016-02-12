M =[[1,2,3],
    [4,5,6],
    [7,8,9]]

col2=[row[1] for row in M]

Diag=[M[i][i] for i in [0,1,2]]

print col2
print Diag
print M
