#IF STATEMENT PRACTICE
num=int(input("enter a number="))
if (num>0):
    print("its a positive number")
#IF ELSE PRACTICE
else:
    print(" Its a negative number")
    #IF ELIF ELSE PRACTICE
if (num>10):
    print("its above 10")
elif(num==0):
    print("its zero")
else:
    print("its less than 10")
#NESTED STATEMENT PRACTICE
#IF ELIF ELSE ELSE INSIDE ANOTHER IF ELIF ELSE
num2=float(input("enter a number="))
if (num2>=0):
    if(num2<=99):
     print("its two digit number")
    else:
     print("is greater than 2  digit number")
else:
    print("its negative number")
    
 
    
