#cube sum of first n natural numbers
n=int(input("enter the number of elements="))
s=0
for i in range(n+1):
 s=s+(i*i*i)
print("the cube of numner from 1 to",n,"is",s)