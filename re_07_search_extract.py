import re
file1=open('mbox-short.txt')

for line in file1:
    line=line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
    	print(line)
