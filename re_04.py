import re
str1='Hello from ikoustou@yahoo.gr to ikoustoude@yahoo.gr about the meeting @2PM'
list1=re.findall('\S+@\S+', str1)

print(list1)
