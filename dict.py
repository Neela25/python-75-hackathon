#Creating 3 dictionaries consisting of student details
student1=dict(name="Neela",regno="16C050",sem=5)
student2={"name":"Meena","regno":"16C040","sem":5}
student3=dict(name="Abi",regno="16C003",sem=5)
#Using setdefault() method,the value for key roll is obtained in n
#Since key roll is not in the dictionary,it is set 
n=student2.setdefault("roll",59057)
#Printing the dictionaries
for i in student1 and student2 and student3:
    print(student1[i],student2[i],student3[i])
#Since roll is only in student2, the loop doesn't print it and it is printed separately
print(student2)

#Output
'''Neela Meena Abi
16C050 16C040 16C003
5 5 5
{'name': 'Meena', 'regno': '16C040', 'sem': 5, 'roll': 59057}'''
