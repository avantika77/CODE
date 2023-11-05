'''Anything can be a lists
Comma separated values
In square brackets
Can be any value, and a mix of values: Integer, Float, Boolean, None, String, List, Dictionary, …
But usually they are of the same type:
Distances of astronomical objects
Chemical Formulas
Filenames
Names of devices
Objects describing attributes of a network device.
Actions to do on your data.'''

#Any layout
'''Layout is flexible
Trailing comma is optional. It does not disturb us. Nor Python.'''

more_stuff = [
  42,
  3.14,
  True,
   None,
   "boo",
    ['another', 'list'],
        {
         'a': 'Dictionary',
         'language' : 'Python',
   },
print(more_stuff)

#Lists
'''Access single element: [index]
Access a sublist: [start:end]
Creates a copy of that sublist'''
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets)   # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print(len(planets))    # 6
print(planets[0])         # Mercury
print(type(planets[0]))   # <class 'str'>
print(planets[3])         # Mars
print(planets[0:1])       # ['Mercury']
print(type(planets[0:1])) # <class 'list'>
print(planets[0:2])       # ['Mercury', 'Venus']
print(planets[1:3])       # ['Venus', 'Earth']
print(planets[2:])        # ['Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets[:3])        # ['Mercury', 'Venus', 'Earth']
print(planets[:])         # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn\ ']

#List slice with steps
''List slice with step: [start:end:step]'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[::])       # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[::1])      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters[::2])      # ['a', 'c', 'e', 'g', 'i']
print(letters[1::2])     # ['b', 'd', 'f', 'h', 'j']
print(letters[2:8:2])    # ['c', 'e', 'g']
print(letters[1:20:3])   # ['b', 'e', 'h']

#Change with steps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers[1::2] = [0, 0, 0, 0, 0, 0]
print(x)    #  ['qqrq', 'xyz', 'dod', 'jkl']
x[1:3] = ['bla']
print(x)    #  ['qqrq', 'bla', 'jkl']
1:2] = ['elp', 'free']
print(x)    # ['qqrq', 'elp', 'free', 'jkl']
#x[1] = ['elp', 'free']
#print(x)    # ['qqrq', ['elp', 'free'], 'jkl']

#Change with steps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers[1::2] = [0, 0, 0, 0, 0, 0]
print(numbers)  # [1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]

#List assignment and list copy
x = ['apple', 'bob', 'cat', 'drone']
y = x
x[0] = 'qqrq'
print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['qqrq', 'bob', 'cat', 'drone']
#There is one list in the memory and two pointers to it.
#If you really want to make a copy the pythonic way is to use the slice syntax.
#It creates a shallow copy.
x = ['apple', 'bob', 'cat', 'drone']
y = x[:]
x[0] = 'qqrq'
print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['apple', 'bob', 'cat', 'drone']

#Deep copy
#from copy import deepcopy
x = ['apple', 'bob', 'cat', 'drone']
y = deepcopy(x)
x[0] = 'qqrq'
print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['apple', 'bob', 'cat', 'drone']

join
fields = ['one', 'two and three', 'four', 'five']
together = ':'.join(fields)
print(together) # one:two and three:four:five
mixed = ' -=<> '.join(fields)
mixed = ' -=<> '.join(fields)
print(mixed) # one -=<> two and three -=<> four -=<> five
another = ''.join(fields)
print(another)  # onetwo and threefourfive

join list of numbers
a = ["x", "2", "y"]
b = ["x", 2, "y"]
print(":".join(a))    # x:2:y
# print ":".join(b)    # TypeError: sequence item 1: expected string, int found
# convert elements to string using map
print(":".join( map(str, b) ))        # x:2:y
# convert elements to string using list comprehension
print(":".join( str(x) for x in b ))  # x:2:y

#split
->Special case: To split a string to its characters: Use the list() function.
->Split using more than one splitter: use re.split
ords = "ab:cd:ef".split(':')
print(words)   # ['ab', 'cd', 'ef']
# special case: split by spaces
names = "foo   bar baz".split()
print(names)   # ['foo', 'bar', 'baz']
# special case: split to characters
chars = list("abcd")
print(chars)   # ['a', 'b', 'c', 'd']

for loop on lists
things = ['apple', 'banana', 'peach', 42]
for var in things:
print(var)

#in list
Check if the value is in the list?
words = ['apple', 'banana', 'peach', '42']
if 'apple' in words:
print('found apple')
if 'a' in words:
print('found a')
else:
print('NOT found a')
if 42 in words:
print('found 42')
else:
print('NOT found 42')

#Where is the element in the list
words = ['cat', 'dog', 'snake', 'camel']
print(words.index('snake'))
print(words.index('python'))

#Index improved
words = ['cat', 'dog', 'snake', 'camel']
name = 'snake'
if name in words:
print(words.index(name))
name = 'python'
if name in words:
print(words.index(name))
#[].insert
words = ['apple', 'banana', 'cat']
print(words)  # ['apple', 'banana', 'cat']
words.insert(2, 'zebra')
print(words)  # ['apple', 'banana', 'zebra', 'cat']
words.insert(0, 'dog')
print(words)  # ['dog', 'apple', 'banana', 'zebra', 'cat']
# Instead of this, use append (next slide)
words.insert(len(words), 'olifant')
print(words)  # ['dog', 'apple', 'banana', 'zebra', 'cat', 'olifant']

#[].append
names = ['Foo', 'Bar', 'Zorg', 'Bambi']
print(names)  # ['Foo', 'Bar', 'Zorg', 'Bambi']
names.append('Qux')
print(names)  # ['Foo', 'Bar', 'Zorg', 'Bambi', 'Qux']

#[].remove
names = ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']
print(names)                # ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']
print(names.remove('Kim'))  # None
print(names)                # ['Joe', 'Jane', 'Bob', 'Kim']
##########################################
'''Remove first element from a list given by its value.
Throws an exception if there is no such element in the list.
------------------------
print(names.remove('George'))
# Traceback (most recent call last):
#   File "examples/lists/remove.py", line 9, in <module>
#     print(names.remove('George'))  # None
# ValueError: list.remove(x): x not in list // "error will be like this"'''

#Remove element by index [].pop
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
print(planets)          # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
third = planets.pop(2)
print(third)            # Earth
print(planets)          # ['Mercury', 'Venus', 'Mars', 'Jupiter']
last = planets.pop()
print(last)             # Jupiter
print(planets)          # ['Mercury', 'Venus', 'Mars']
# planets.pop(4)          # IndexError: pop index out of range
jupyter_landers = []
# jupyter_landers.pop()   # IndexError: pop from empty list
#Remove and return the last element of a list. Throws an exception if the list was empty.
Remove first element of list
{To remove an element by its index, use the slice syntax:}-----------------------------
names = ['foo', 'bar', 'baz', 'moo']
first = names.pop(0) {index 0} 
print(first)    # foo #output
print(names)    # ['bar', 'baz', 'moo'] #output
Remove several elements of list by index
To remove an element by its index, use the slice syntax:
names = ['foo', 'bar', 'baz', 'moo', 'qux']
names[2:4] = []
print(names)    # ['foo', 'bar', 'qux']

#Use list as a queue
a_queue = []
print(a_queue)
a_queue.append('Moo')           
print(a_queue)                    
a_queue.append('Bar')
print(a_queue)
first = a_queue.pop(0)
print(first)
print(a_queue)

Queue using deque from collections
from collections import deque
# items = deque([])
items = deque(['foo', 'bar'])
print(type(items))  # <type 'collections.deque'>
print(items)        # deque(['foo', 'bar'])
items.append('zorg')
print(items)        # deque(['foo', 'bar', 'zorg'])
print(len(items))   # 3
if items:
print("The queue has items")
else:
 prit("The queue is empty")
[.append
.popleft
len() number of elements
if q: to see if it has elements or if it is empty
dequeue]
Fixed size queue
 1 from collections import deque
 2 
 3 queue = deque([], maxlen = 3)
 4 print(len(queue))     # 0
 5 print(queue.maxlen)   # 3
