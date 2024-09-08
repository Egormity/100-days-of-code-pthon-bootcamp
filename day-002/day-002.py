# --- DATA TYPES ---

# --- 1. String ---
# print('Hello'[-1])
# print('5' + '5')

# --- 2. Integer ---
# print(5 + 5)

# --- 3. Float ---
# 3.14159

# print(type(123))
# nameLength = len(input('Enter your name: '))
# print('Your name length: ' + str(nameLength))

# number = input('Enter 2 digit number: ')
# print('Sum of digit = ' + str(int(number[0]) + int(number[1])))

# print(3 ** 3)
# print( 11 % 2)

# --- BODY MASS INDEX ---
# weight = input('Enter your weight (in kg): ')
# height = input('Enter your height (in m): ')
# bmi = float(weight) / float(height) ** 2
# print(bmi)

# print(round(8 / 3, 2))
# print(8 // 2)

# num = 10
# num += 5
# print(num)

# --- F strings ---
# print(f"Hello {num}")

# bool = True
# print(bool)

# --- LIFE I WEEKS ---
# age = input("What is your current age? ")
# years = 90 - int(age)
# weeks = years * 52
# days = weeks * 7
# print(f"You have left {years} years or {weeks} weeks or {days} days")

# --- FINAL PROJECT - TIP CALCULATOR ---
print('Welcome to the tip calculator')
totalBill = float(input('What was the total bill?: $'))
tipPercentage = float(input("what percentage tip would you like to give?: %"))
peopleNum = float(input("How many people to split the bill?: "))
print(f"Each person should pay ${round((totalBill + (totalBill * (tipPercentage / 100))) / peopleNum, 2)}")