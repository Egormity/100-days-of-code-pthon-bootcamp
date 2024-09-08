import random

# randomInt = random.randint(1, 10)
# print(randomInt)

# randomFloat = random.random() * 10
# print(randomFloat)

# list = [1, 2, 3, 4, 5]
# list.append(6)
# list.extend(["Hello", 'Bro'])
# print(list)

# --- WHO'S PAYING FOR MEAL ---
# people = input('Write people why ate separated  by comma: ').split(', ')
# # whyPay = people[random.randint(0, len(people) - 1)]
# whyPay = random.choice(people)
# print(f'{whyPay} is going to pay for meal today!')

# --- ROCK, PAPER, SCISSORS ---
# list = [
# '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''',

# '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# ''',

# '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# ]

# user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ').lower())
# computer = random.randint(0, 2)

# if user < 0 or user > 2:
#     print('You typed an invalid number, you lose!')
#     exit()

# print(f'You chose: {list[user]}')
# print(f'Computer chose: {list[computer]}')

# if user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
#     print('You win!')
# elif computer == 0 and user == 2 or computer == 1 and user == 0 or computer == 2 and user == 1:
#     print('You lose!')
# else:
#     print('Draw!')