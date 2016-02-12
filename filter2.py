maths_grades=[1,7,5,3,8,4]
physics_grades=[2,10,4,2,9,8]
history_grades=[3,7,2,6,10,6]

pupils=list(zip(maths_grades,physics_grades,history_grades))

def passall_func(*a):
    print(*a)
    for i in range(len(a)):
        print(a[i])
        if a[i]<5:
            return False
            break
    else:
        return True
    


passall=list(filter(passall_func, pupils))

print(passall)
