#Range function with 2 arguments.
#The first argument is the starting value and second argument is the stop value
#This program takes an input number and prints a sequence of numbers from 123..n
print("Enter a number:")
n=int(input())
n=n+1
nums=[]
#The above line creates an empty list
#The following for loop appends the numbers from 1 to n to the list
for i in range(1,n):
    nums.append(i)
print(*nums, sep='')
#The above line takes out all the commas and barackets in the list and prints the output

#Output
# Enter a number:
# 5
# 12345
