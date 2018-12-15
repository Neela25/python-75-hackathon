#Debugging basics--Importing package python debugger
import pdb
def reverse(n):
#Suppose we want to begin the trace of code here and it is done using set_trace()
    pdb.set_trace()
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
n=int(input("Enter the number:"))
print("The reversed number is ",reverse(n))

#Output
'''
Enter the number:1234
> c:\users\varsha\desktop\pjs\python\reverse.py(6)reverse()
-> rev=0
(Pdb) n  #To pass through the code line by line
> c:\users\varsha\desktop\pjs\python\reverse.py(7)reverse()
-> while n>0:
(Pdb) n
> c:\users\varsha\desktop\pjs\python\reverse.py(8)reverse()
-> rem=n%10
(Pdb) l #To know currently we are in which line of the code
  3  	def reverse(n):
  4  	#Suppose we want to begin the trace of code here and it is done using set_trace()
  5  	    pdb.set_trace()
  6  	    rev=0
  7  	    while n>0:
  8  ->	        rem=n%10
  9  	        rev=rev*10+rem
 10  	        n=n//10
 11  	    return rev
 12  	n=int(input("Enter the number:"))
 13  	print("The reversed number is ",reverse(n))
(Pdb) n
> c:\users\varsha\desktop\pjs\python\reverse.py(9)reverse()
-> rev=rev*10+rem
(Pdb) n
> c:\users\varsha\desktop\pjs\python\reverse.py(10)reverse()
-> n=n//10
(Pdb) n
> c:\users\varsha\desktop\pjs\python\reverse.py(7)reverse()
-> while n>0:
(Pdb) c  #Returning to normal execution
The reversed number is  4321
>>> 
'''
