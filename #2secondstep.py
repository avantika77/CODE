#modules
import sys
print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)

print(sys.getsizeof(3))
print(sys.getsizeof(34))
print(sys.getsizeof(3.8))
print(sys.getsizeof(""))
print(sys.getsizeof("s"))
print(sys.getsizeof("hi"))
print(sys.getsizeof("hello"))

def main():
    print("hogwarts")
    print("legacy")
print("before")
main()
print("after")

#def main():
 # print("games")
# if_name_ == "_main_"
#    main()
    
val=input("type in a decimal:")
print(val)
print(val.isdecimal())
print(val.isdecimal())
if val.isdecimal():
    num=int(val)
    print(num)
    
   #converting string to integer 
a=23
print(a)
print(type(a))
#<class 'str'>

# converting float to int
a=2.1
print(type(a))
#<class 'float'>
print(a)

#conditons:if
def  main():
    expected_answer = 45
    inp=input("Please enter the answer:")
    if inp==expected_answer:
        print("welcome")
        main()
   
   #condition :if else:   
# def main():
#      a = input('First number: ')
#      n = input('Second number: ')
# if int(n) == 0:
#         print("Cannot divide by 0")
# else:
#      print("Dividing", a, "by", n)
#      print(int(a) / int(n))

#condition:elif
# def main():
#     a=input('First number: ')
#     b=input('Second number: ')
# if a==b:
#     print("they are equal")
# elif int(a) < int (b):
#     print(a + "is smaller than b" + b)
# else:
#     print(a + "is biggger than b" + b)
#     main()
    
#ternary operator    
x = 3
answer = 'positive' if x > 0 else 'negative'
print(answer) 

#script that will ask for the sides of a rectangular and print out the area.
def main():
    length = int(input('Length: '))
    width = int(input('Width: '))
    if length<=0:
        print ("width not positive")
        return
    area =length*width
    print ("the area is", area)
    main() 
    
    #calculator
# main()
 def main():
     a = input("Number: ")
    b = input("Number: ")
    op = input("Operator (+-*/): ")
    command = a + op + b
    print(command)
    res = eval(command)
    print(res)



