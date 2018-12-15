#Importing the module calc
import calc
#Getting user input
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1-Addition  2-Subtraction  3-Multiplication  4.Divisoin  5.Power")
while True:
    c=int(input("Enter Choice:"))
    if c>5:
        break
    else:
#Using the function calculator in calc module to perform the action
        print("The result is ",calc.calculator(a,b,c))



#Output
'''Enter first number:5
Enter second number:5
1-Addition  2-Subtraction  3-Multiplication  4.Divisoin  5.Power
Enter Choice:5
The result is  3125
Enter Choice:3
The result is  25
Enter Choice:4
The result is  1.0
Enter Choice:6
>>> '''
