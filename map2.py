mathites=[
	dict(id=0, name='John', age=40, history=10, maths=8),
	dict(id=1, name='Stella', age=35, history=5, maths=9)
]

#print(mathites)

print (mathites[0])
print()
print(mathites[0]['history'] , mathites[0]['maths'])

def decorate(student):
	sum1=student['history']+student['maths']
	return (sum1, student)  #2-tulpe

def undecorate(stu):
	return stu[1]        #return original student without sum


mathites = sorted(map(decorate, mathites) , reverse=True) #sorted 1 column aca sum1

print(mathites)
print()

mathites=list(map(undecorate, mathites))

print(mathites)
print()
