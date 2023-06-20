#calculate BMI (body mass index)
#formula(bmi=weight/height**2)
weight=input("enter the value of wight in kg=")
height=input("enter the value of height in m=")
print(type(weight))
print(type(height))
bmi=(int(weight)/(float(height))**2)
print("the bmi value is",bmi)
#roundoff of negative 
print("The round of negative")
print(round(3235,-5))
print(round(-7893,2))

#Calculating BMI WITH SOME CONDITION
weight=float(input("enter  weigth in kg:"))
height=float(input("enter  height in m:"))
bmi=weight/height**2
if bmi <18.5:
    print(f"you have {bmi} and you are underweight")
elif bmi < 25:  
    print(f"you have {bmi} and you have normal weight")
elif bmi < 30:  
    print(f"you have {bmi} and you have overweight ")
elif bmi < 35:  
    print(f"you have {bmi} and you are obese")
else :  
    print(f"you have {bmi} and you are clinically obese")
