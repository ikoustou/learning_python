def foo(a=[]):
        #print (a)
        print('\n', len(a))
        a.append(len(a)*10)
        print(a)

foo()                 #prints [0]
foo()                 #prints [0,10]
foo( [12,13,14] )     #prints [12,13,14,30]
foo()                 #prints [0,10,20]
