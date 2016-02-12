a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

grades=list(zip(a,b,c))
for i in range(len(grades)):
    print(grades[i])

print(max(*grades[0]) )

maxlist=list(map(lambda a: max(*a), grades))
print(maxlist)

