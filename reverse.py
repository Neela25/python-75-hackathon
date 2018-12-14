#A function to reverse a given input number
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
print("Enter the number:")
n=int(input())
print("The reversed number is ",reverse(n))

#Output
#Enter the number:
#12345
#The reversed number is  54321
