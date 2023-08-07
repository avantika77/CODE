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




