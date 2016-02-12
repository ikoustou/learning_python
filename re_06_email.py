import re
file1=open('mbox-short.txt')

for line in file1:
    line=line.rstrip()
    list1=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(list1)>0:
        print(list1)
