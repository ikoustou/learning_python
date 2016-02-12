import re
file1=open('mbox-short.txt')

for line in file1:
	line = line.rstrip()  #dioxnei ta kena
	if re.search('From:', line):
		print(line)


