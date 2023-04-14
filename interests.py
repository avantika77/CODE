#simple and compund interests
p=int(input("enter the principal="))
r=int(input("enter the rate="))
t=int(input("enter the time="))
SI= si = (p * t * r)/100
print("the simple interest is ",SI)
Amount = p * (pow((1 + r / 100), t))
CI = Amount - p
print("Compound interest is", CI)