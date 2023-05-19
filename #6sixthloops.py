#Loops: for-in and while
#for in - to iterate over a well defined list of values.while - repeate an action till some condition is met. (or stopped being met)
txt = 'hello world'
for c in txt:
    print(c)
    
 #for-in loop on list
for fruit in ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]:
   print(fruit)

#for-in loop on
for i in range(3, 7):
    print(i)

#Iterable, iterator
#for in loop with early end using break
txt = 'hello world'
for c in txt:
   if c == ' ':
      break
   print(c)

#for in loop skipping parts using continue
txt = 'hello world'
for c in txt:
    if c == ' ':
       continue
    print(c)
    
#for in loop with break and continue
txt = 'hello world'
for cr in txt:
 if cr == ' ':
       continue
 if cr == 'r':
      break
print(cr)
print('DONE')

#while loop
import random
total = 0
while total <= 100:
 print(total)
 total += random.randrange(20)
 print("done")

#Infinite while loop
'''import random
total = 0
while total >= 0:
 print(total)
 total += random.randrange(20)
 print("done")'''
 #Use Ctrl-C to stop it

 #While with complex expression
import random
total = 0
while (total < 10000000) and (total % 17 != 1) and (total ** 2 % 23 != 7):
   print(total)
   total += random.randrange(20)
print("done")

#While with break
import random
total = 0
while total < 10000000:
 print(total)
 total += random.randrange(20)
 if total % 17 == 1:
   break
 if total ** 2 % 23 == 7:
  break
print("done")




    
 
