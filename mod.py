import calc
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1-Addition  2-Subtraction  3-Multiplication  4.Divisoin  5.Power")
while True:
    c=int(input("Enter Choice:"))
    if c>5:
        break
    else:
        print("The result is ",calc.calculator(a,b,c))
