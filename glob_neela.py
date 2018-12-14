#This function will return the sum of digits of number 123 for whatever the number is being given as input
def sum_of_digits():
#Here the global variable is used and hence the keyword global is used
    global n
    n=123
    temp=n
    s=0
#The while loop computes the sum of digits
    while temp>0:
        rem=temp%10
        s=s+rem
        temp=temp//10
    return s
#Getting input
print("Enter the number:")
#A global variable
n=int(input())
#The value of n that is got as input is printed.
print(n)
#Function call to compute the sum of digits
ans=sum_of_digits()
#Prints the sum for the number 123 by deafult as it has been modified in the function
print("The sum of digits of ",n,":",ans)


#Output
'''nter the number:
1234
1234
The sum of digits of  123 : 6 '''
