#A function to count the number of inputs in the given tuple
def count(tupl):
    print("Enter a number:")
    n=int(input())
#Checking whether the number is in the tuple    
    if n in tupl:
#Counting the number of occurences of n using count() function
        c=tupl.count(n)
        print("The number of ",n,"'s in tuple is",c)
#If the number is not found print it
    else:
        print("Number not found in tuple")
#Creating a tuple using the tuple() constructor        
tup=tuple((25,76,25,50,30,1,24,25,16,12,16,25))
#Calling the function
count(tup)

#Output
'''
Enter a number:
25
The number of  25 's in tuple is 4'''

'''
Enter a number:
80
Number not found in tuple'''

