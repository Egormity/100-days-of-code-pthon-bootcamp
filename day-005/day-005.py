import random

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# --- AVERAGE ---
# heights = [170, 180, 190, 200]
# sum = 0
# for height in heights:
#     sum += height
# average = sum / len(heights)
# print(average)

# --- HIGHEST SCORE ---
# scores = [10, 20, 30, 120, 50, 60, 70, 80, 90, 100]
# highest = scores[0]
# for score in scores:
#     if score > highest:
#         highest = score
# print(highest)

# sum = 0
# for i in range(2, 101, 2):
#     # if i % 2 == 0:
#         sum += i
# print(sum)

# --- FIZ BUZZ GAME ---
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     if i % 3 == 0:
#         print('Fizz')
#     if i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# --- RANDOM PASSWORD ---
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# charactersLength = int(input('Enter password length: '))
# symbolsAmount = int(input('Enter number of symbols: '))
# numbersAmount = int(input('Enter number of numbers: '))

# if (symbolsAmount + numbersAmount) > charactersLength:
#     print('Symbols and numbers cannot be more than password length')
#     exit()

# passwordNotRandomized = []

# for index, number in enumerate(numbers):
#     if index > numbersAmount:
#         break
#     passwordNotRandomized.append(random.choice(numbers))

# for index, symbol in enumerate(symbols):
#     if index > symbolsAmount:
#         break
#     passwordNotRandomized.append(random.choice(symbols))

# for letter in letters:
#     if len(passwordNotRandomized) >= charactersLength:
#         break
#     passwordNotRandomized.append(letter)

# password = ''
# for i in range (charactersLength):
#     password += random.choice(passwordNotRandomized)

# print(password)