







name = input("What is your name? : ")

# Input month and day
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))

# Check for invalid data
if month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid data entered.")
elif month < 10 or (month == 10 and day < 31):
    print(f"{name}, your birthday is before Halloween.")
elif month == 10 and day == 31:
    print(f"{name}, your birthday is special. It's on the same as Halloween!")
else:
    print(f"{name}, your birthday is after Halloween.")
