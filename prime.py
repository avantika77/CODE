number=int(input("enter your favourite number:"))
if number>1:
    for i in range(2, number):
        if(number%i==0):
          print(number,"is not prime number")
          break
    else:
          print (number,"is prime")