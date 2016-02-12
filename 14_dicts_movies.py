table = {'1975' : 'Holy Grail',
		 '1979' : 'Life of Brian',
		 '1983' : 'The meaning of Life'}

year = '1983'
movie = table[year]
print movie
print
for year in table:
        print(year + '\t'+ table[year])
        
