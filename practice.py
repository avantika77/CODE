import sys
print(sys.version)
print(sys.version)

#containing the value in a variable
i=7
print("the value of i",i)
print("i repeat,the value is",i)

#comment in python 
print("avantika")
''' this is comment
print("my name")
print("this is still comment")'''

#indentation example done 
#variable and data structures
counter=100    #an interger assignment
miles=1000.0   #a floating assignment
name="ajay"     # a string
print(counter);print(miles);print(name)

a= 11111111
b=2.0
c="0"
d="sai"
print (name)
print (a)
print(b+a)
print(c+d) #concatinating string value
 
 #string 
str='hello world'
print(str)
print(str[0])
print(str[2:7])
print(str[2:])
print(str*2)
print(str[:-3])
print("sai".join([str]*9))
print(str +' '+ str +'')
print(str+"test") #print concatenated string

str="hello"
print(str[-4])
a='this is a string'
a=a.replace('','')

a='sai'
print(a+a)
a=23.2
#anum =int(a)       # typecast /convert string '20' to integer
#print (anum +anum)
anum=(int(a))
#print(anum+anum)
a=34.9
print (a+a)
anum=int(a)

a=(1,2,3, ['acc',124]) #list inside tuple
a[3][1]=10
print(a)
 
 #how to create formated outputs
str=("this is python")
strlist=list(str)
print(str)
print(strlist)
#print(strlist.sort()) 
a=sorted(strlist)
print(a)


school='ISB'
print('S' in school) #boolean question
print('S' in school)

#swipping first three string of character and join them by an _
x="mousedown"
y="trap"
string=str(x[:3])
print(string)
string2 = string(y[:3])
print(string2)
print (string2 + x[3:] + "_" + string +  y[:3] ) 


