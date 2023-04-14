#palindrome same from forward and backward
#used slicing string ::-1 as not specifying first and mid value 
a=input("enter a string=")
reverse=a[::-1]
if(reverse==a):
    print("Its a palindrome number")
else:
       print("Its not a palindrome number")