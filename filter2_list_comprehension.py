maths_grades=[1,7,5,3,8,4]
physics_grades=[2,10,4,2,9,8]
history_grades=[3,7,2,6,10,6]

pupils=list(zip(maths_grades,physics_grades,history_grades))

print(pupils)
    


passall=[(a,b,c) for a,b,c in pupils if min(a,b,c)>4]

print(passall)
