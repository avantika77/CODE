lst=[]
num=int(input("Enter the numbers od elements for the list:"))
for n in range(num):
    numbers=int(input("enter the numbers:"))
    lst.append(numbers)
print("maximum element in the list is" ,max(lst))
      