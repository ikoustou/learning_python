import re
file1=open('mbox-short.txt')

for line in file1:
    line=line.rstrip()

    # oi parentheseis tha exagoun to noumero-string
    list1= re.findall('^X\S*: ([0-9.]+)', line)
    if len(list1)>0:
        print(list1)
