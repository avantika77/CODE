a=2.4 #decimal
h=0xa #hexa
o=0o11
b=0b11
r=12
print(a)
print(h)
print(o)
print(b)
print(r)

a=2
b=3
c=2.3
d=a+b
print(b//a) #floor division
print(a*c)
print(a**b) #power
print(17%3) #modulus division
a+=7
#a++  #syntax error invalid syntax
#a-- #syntax error invalid syntax
a+=1
print(a)
a-=1
print(a)

print(3/2) 
print (int(3/2))  #python3 use of integer

#pseudo random number
import random
a=random.random()
print (a)
print(random.random())
print(random.random())
random.seed(45)
print(random.random())

#rolling dice-randrange
import random
print(1+int(6*random.random()))
print(random.randrange(1,7)) #anyone of the following :1,2,3,4,5,6,7

#random choice
import random
letters="adjhfhdjkfdskjfhu"
print(random.choice(letters))
fruits=["papaya","apple","orange","peach","banana"]
print(random.choice(fruits))

#build-in method
import random
rnd=random.random
print(rnd)  # <built-in method random of Random object at 0x124b508>
y=rnd
print(y)

#A commont mistake. Calling the class and not the method
'''import random
print ("hello")
x=random()
print(x) '''

from random import random
x = random()
print(x)

'''Using the random module the computer “thinks” about a whole number between 1 and 20.
The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
The game ends after just one guess'''
import random
hidden = random.randrange(1,20)
print ("the hidden values is ", hidden)
user_input=input ("please enter your guess=")
guess=int(user_input)
if guess==hidden:
    print("hit!")
elif guess < hidden :
    print ("your guess is too low")
else:
    print("your guess is too high")
    

#Write a script that will pick 3 fruits from a list of fruits like the one we had in one of the earlier slides. Print the 3 names.
import random 
fruits =["apple", "orange", "peach","papaya"]
salad=random.sample(fruits,3)
print(salad)








