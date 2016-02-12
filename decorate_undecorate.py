students = [
dict(id=0, credits=dict(math=9, physics=6, history=7)),
dict(id=1, credits=dict(math=6, physics=7, latin=10)),
dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(stu):
    """Create a 2-tuple (sum of credits, student) from stu dict"""
    return (sum(stu['credits'].values()) ,stu)

def undecorate(decor_stu):
    """discard sum of credits, return original student dict"""
    return decor_stu[1]

students = sorted( map(decorate, students), reverse=True)
students = list (map(undecorate, students) )

print (students)



