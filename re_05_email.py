import re
file1=open('mbox-short.txt')

for line in file1:
    line=line.rstrip()
    list1=re.findall('\S+@\S+', line)
    if len(list1)>0:
        print(list1)
