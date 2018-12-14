#Opening a file
#2 arguments- file name and the mode,here read mode
fp=open("sample.txt","r")
#Reading and printing the contents
print(fp.read())
print("---------------------------------------------")
#End of file has been reached.So start from begining using seek()
fp.seek(0)
#Reading and printing again
print(fp.read())

#Output

'''
================== RESTART: C:/Users/Varsha/Desktop/file.py ==================
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

---------------------------------------------
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

'''
