#This program generates a random number from a choice of a list specified and removes it from the list
import random
list=[1,2,3,4,5,9,6,8,0]
#The choice() function is used to generate random numbers from the list above
#The random number is stored in a variable
n=random.choice(list)
#Random number is printed
print("The random number is ",n)
#Removed from the list
list.remove(n)
print(list)


#Output
#The random number is  6
#[1, 2, 3, 4, 5, 9, 8, 0]
