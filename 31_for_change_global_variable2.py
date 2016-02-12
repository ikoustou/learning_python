A=100
print(A)

colect=[A for A in range(10)] # den allazei tin global A

for i in range(len(colect)):
    print(colect[i])

print()
print(A)


A = 100
ex1 = [A for A in range(5)]
print(A)
