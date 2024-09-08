# --- EVEN OR ODD ---
# num = int(input('Enter your number: '))
# if num % 2 == 0:
#     print('Your number is even')
# else:
#     print('Your number is odd')

# --- ROLLERCOASTER ---
# height = int(input('Enter your height in cm: '))
# age = int(input('Enter your age: '))
# bill = 0

# if height > 120:
#     print('You can ride the rollercoaster')
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print('Everything is going to be OK. Have a ride on us!')
#     else:
#         bill = 12
    
#     isPhoto = input ('Do you want a photo taken? Yes or No: ')
#     if isPhoto == 'Yes':
#         bill += 3
#     print(f'Your final bill is ${bill}')
# else:
#     print('Sorry, you have to grow taller before you can ride the rollercoaster')

# --- BMI ---
# bmi = 20
# if bmi < 18.5:
#     print('Underweight')
# elif bmi < 25:
#     print('Normal')
# elif bmi < 30:
#     print('Overweight')
# elif bmi < 35:
#     print('Obese')
# else:
#     print('Obese')

# --- LEAP YEAR ---
# year = int(input("Input your year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f'{year} is a leap year')
#         else:
#             print(f'{year} is not a leap year')
#     else:
#         print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')

# --- PIZZA ORDER ---
# print('Welcome to Python Pizza Delivery!')
# size = input('What size pizza do you want? S, M, or L: ')
# addPepperoni = input('Do you want pepperoni? Y or N: ')
# extraCheese = input('Do you want extra cheese? Y or N: ')

# bill = 0
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25

# if addPepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3

# if extraCheese == 'Y':
#     bill += 1

# print(f'Your final bill is: ${bill}')

# -- operators in python: 'and' 'or' 'not' ---
