# 1st way
kg=42
name='wheat'
str_concatenate=" the user has " +  str(kg)  +  "of" + name
print(str_concatenate)

# 2nd way
str_concatenate="the user  %s  has  %s." %(name, str_concatenate)
print(str_concatenate)

# 3rd way
str_format= "the user has {} of {}.".format(kg, name)
print (str_format) 

# 4the way
str_f_string=f" the user has {kg} of {name}."
print(str_f_string)

# using format - indexing
text="Shyam"
numb=1996
print( "The user {0} was born in {1}.".format(text, numb))
print( "The year is {1} in which the user was born {0}.".format(text,numb))

#using name
print("the year is {age} in which {name} was born.".format(name=text, age=numb))

#format column
data=[
    ["agnes", 18],
    ["gloriya",20],
    ["mert",21878],
    ["destiny goods",4],
    ["joe",685854998797],
]
for entry in data:
    print("{} {}".format(entry[0],entry[1]))

print('_' * 16)
for entry in data:
    print("{:<8} | {:>7}".format(entry[0],entry[1]))
    
#using format -alignment
txt=" hello agnes"
print ("'{}'".format(txt))
print ("'{:12}'".format(txt))
print ("'{:<12}'".format(txt))
print ("'{:>12}'".format(txt))
print ("'{:^12}'".format(txt))

#format string
name="hello loco"
print("{:s}".format(name))
print("{}".format(name))

#Format characters and types
x = 67
print("{:b}".format(x))
print("{:c}".format(x)) 
print("{:d}".format(x))   
print("{:o}".format(x)) 
print("{:x}".format(x)) 
print("{:X}".format(x)) 
print("{:n}".format(x)) 
print("{}".format(x))  

#Format floating point number
x = 412.345678901
print("{:e}".format(x))   
print("{:E}".format(x))  
print("{:f}".format(x))   
print("{:.2f}".format(x)) 
print("{:F}".format(x))   
print("{:g}".format(x))
print("{:G}".format(x))  
print("{:n}".format(x))   
print("{}".format(x))    

#f-strings (formatted string literals)
name = "Foo Bar"
age = 42.12
pi = 3.141592653589793
r = 2
print(f"The user {name} was born {age} years ago.")
print(f"The user {name:10} was born {age} years ago.")
print(f"The user {name:>10} was born {age} years ago.")
print(f"The user {name:>10} was born {age:>10} years ago.")
print(f"PI is '{pi:.3}'.")   # number of digits (defaults n = number)
print(f"PI is '{pi:.3f}'.")  # number of digits after decimal point
print(f"Area is {pi * r ** 2}")
print(f"Area is {pi * r ** 2:.3f}")

#printf using old %-syntax
v = 65
print("<%s>" % v)     # <65>
print("<%10s>" % v)   # <      65>
print("<%-10s>" % v)  # <65      >
print("<%c>" % v)     # <A>
print("<%d>" % v)     # <65>
print("<%0.5d>" % v)
