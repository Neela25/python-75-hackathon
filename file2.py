from collections import Counter
#Opening a file in read mode
fp=open("sample.txt","r")
count=0
#Split each line into words and store it in w
#Counting the number of words which is the length of w and adding it to a variable
for j in fp:
    w=j.split()
    print(w)
    print(len(w))
    count=count+len(w)
print("The number of words:",count)
#Output
'''
['What', 'can', 'Python', 'do?']
4
['Python', 'can', 'be', 'used', 'on', 'a', 'server', 'to', 'create', 'web', 'applications.']
11
['Python', 'can', 'be', 'used', 'alongside', 'software', 'to', 'create', 'workflows.']
9
['Python', 'can', 'connect', 'to', 'database', 'systems.', 'It', 'can', 'also', 'read', 'and', 'modify', 'files.']
13
['Python', 'can', 'be', 'used', 'to', 'handle', 'big', 'data', 'and', 'perform', 'complex', 'mathematics.']
12
['Python', 'can', 'be', 'used', 'for', 'rapid', 'prototyping,', 'or', 'for', 'production-ready', 'software', 'development.']
12
The number of words: 61
'''
