#text inside pair of qoutes single or double
soup="spices carrot lentil soup"
print (soup)
#long line
text="abc"  "def"
print (text)
long_string= "adjg" "dwdd" "efdeq"
print(long_string)
#short row
short_rows = "one" \
    "two" \
    "three"
print(short_rows)
#long_string
long_string="first seconf third row "
print(long_string)
#triple qoutes string
text="""first row
second row
third row"""
print(text)
#string length
line="hello learner"
hw=len(line)
print(hw)
text="""hello
learners"""
print(len(text))

#string repetiton and concatation
name = 2 * 'Jar '
print(name)          
full_name = name + 'Binks'
print(full_name)  
title = "We have some title"
print(title)
print('-' * len(title))

#A character in a string
text = "Hello World" 
a = text[0]
print(a)      
b = text[6]
print(b)   

#String slice (instead of substr)
text = "Hello World"
b = text[1:4]
print(b)         
print(text[2:])   # llo World
print(text[:2])   # He
start = 1
end = 4
print(text[start:end])

#Python strings are “immutable”, meaning you cannot change them You can replace a whole string in a variable, but you cannot change it.
text = "abcd"
print(text)    
text[2] = 'Y'
print("done")
print(text)

#how to change a string
text = "abcd"
print(text)      
text = text[:2] + 'Y' + text[3:]
print(text)      

#String copy
text = "abcd"
print(text)     
text = text + "ef"
print(text)    
other = text
print(other)     
text = "xyz"
print(text)     
print(other)   

#String functions and methods (len, upper, lower)
a = "xYz"
print(len(a))     
b = a.upper()
print(b)          
print(a)          
print(a.lower())

#index in string
text = "The black cat climbed the green tree."
print(text.index("bl"))    
print(text.index("The"))    
#print(text.index("dog"))

#index in string with range
text = "The black cat climbed the green tree."
print(text.index("c"))     
print(text.index("c", 8))   
print(text.index("gr", 8))      
#print(text.index("gr", 8, 16))

#find in string
#Alternatively use find and rfind that will return -1 instead of raising an exception.
text = "The black cat climbed the green tree."
print(text.find("bl"))    
print(text.find("The"))   
print(text.find("dog"))    
print(text.find("c"))     
print(text.find("c", 8))  
print(text.find("gr", 8))      
print(text.find("gr", 8, 16))  
print(text.rfind("c", 8))   

#in string
txt = "hello world"
if "wo" in txt:
 print('found wo')
if "x" in txt:
  print("found x")
else:
    print("NOT found x")
    
#index if in string
sub ="cat"
txt="the black cat climes the green tree"
    if sub in txt:
      loc=txt.index(sub)
      print(sub+"is at " +str(loc))
    sub="dog"
    if sub in txt :
      loc =txt .index(sub)
    print(sub+"is at " +str(loc))
    
  #ord 
    print( ord ("a"))
    print( ord ("="))
    print( ord ("\r"))
    print( ord ("\n"))
    print( ord (" "))
    print( ord ("a"))
    print( ord ("o"))
    print( ord ("#"))
    
#ord in a life
#import sys
#filename=sys.argv[1]
#with open (filename) as fh:
 #for c in content:
  #print (ord (c))
  
#char number to charcter
for i in range (23,125):
  print(i,chr(i))
  
#one string in another string 
    
    
    



