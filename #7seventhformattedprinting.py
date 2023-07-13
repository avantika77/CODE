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



