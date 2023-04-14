#Find all numbers which are multiple of 17, but not the multiple of 5, between 2000 and 2500
for i in range (2000,2500):
    if (i%7==0 and i%5!==0):
        print("numbers=",i)

