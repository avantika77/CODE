''Halloween Assignment 

October 31st is a special date. It’s Halloween! Write a program that determines if someone’s birthday is on the same day as Halloween. 
Ask the user to enter their name, a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on October 31st. 

●	If the date occurs before October 31st , output their name and a sentence with the word “before”. 
●	If the date occurs after October 31st, output their name and a sentence with the word “after”. 
●	If the date is October 31st, output their name and a sentence with the word  “Special”.
●	If the month entered is not between 1 and 12, display only “Invalid data entered.” 
●	If the day entered is not between 1 and 31, display only “Invalid data entered.”
●	Assume all data entered are integers.

Input / Output should look exactly like below

Sample Input 1
What is your name? : Abid  ( Bold means input from the user )
Please enter a month: 2
Please enter a day: 20

Output for Sample Input 1
Abid, your birthday is before Halloween.
 
Sample Input 2
What is your name? : Tyler
Please enter a month: 10
Please enter a day: 31

Output for Sample Input 2
Tyler, your birthday is special. It’s on the same as Halloween!

Sample Input 3
What is your name? : Ella
Please enter a month: -5
Please enter a day: 30

Output for Sample Input 3
Invalid data entered.'''

#--------------------------------------------------------------------------------------------------------------------------------------------
name = input("What is your name? : ")
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))

#logic
if month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid data entered.")
elif month < 10 or (month == 10 and day < 31):
    print(f"{name}, your birthday is before Halloween.")
elif month == 10 and day == 31:
    print(f"{name}, your birthday is special. It's on the same as Halloween!")
else:
    print(f"{name}, your birthday is after Halloween.")

#Output#--------------------------------------------------------------------------------------------------------------------------------------
What is your name? : avi
Please enter a month: 10
Please enter a day: 31
avi, your birthday is special. It's on the same as Halloween!

What is your name? : D
Please enter a month: 13
Please enter a day: 33
Invalid data entered.
