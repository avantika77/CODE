#if statement
x=2
if x==2:
    print("it is 2")
else:
    print("its is not 2")
 
#true of false are real boolean values.
x=2
v=x==2
print(v)
if v:
    print (v,"is true")
else:
    print(v,"is false") 

#boolean
x=23
if x:
    print("23 is true")
else:
    print("23 is false")
y=0
if x:
    print("0 is true")
else:
    print("0 is false")
    
#true and false value in python
value=[None,0,"",False,[],{},() ,"0",True] #none,false, true is keyword will be with capital start
#none is like nill or null,undef in other language
for v in value :
    if v:
        print("true value: ", v)
    else:
        print("false value: ", v)
    
#comparision operators
a="23"
b=76
print(a==b)             #answers wiil be in boolean
print(a!=b)
print(b==76.3)
print(None==None)
print(None==False)

#do not compare different type
x=66
y=66
print(x==y)
x=12
y="3"  
print(x==y)

#boolean operaors= and ,or and not
#short circuit 
'''def money():
 return money > 100000
def check_salary():
    salary+=1
    return (salary >= 1000)
while True :
      has_good_money=money()
      has_good_salary=check_salary()
      if has_good_money or check_salary:
        print("i can live well")'''

#if status_code==401 or 393:
#pass

#Ask the user to enter two numbers and tell us which one is bigger.
a=int(input("enter a number="))
b=int(input("enter a number="))
if(a>b):
    print("a is bigger")
if(a<b):
    print("b is bigger")
else :
    print("both are equal")
    
#compare strings    
a=input("enter a string=")
b=input("enter a string =")
print("now tell how you want to compare:")
print("(1) ASCII BASE")
print("(2) LENGHT BASE")
how=input()
if how =="1":
   first= a > b
   second=a<b
elif how =="2":
    first=len (a)< len(b)
    second=len(a)>len(b)
    if first:
     print("First number is bigger")
    elif second:
     print("First number is smaller")
    else:
     print("They are equal")

