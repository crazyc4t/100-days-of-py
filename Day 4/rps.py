import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# My code

bet = [rock, paper, scissors]
choice = random.randint(0, 2)
playersbet = input("What do you choose? 0 = rock, 1 = paper, 2 = scissors ")

if playersbet == '0' and choice == 0:
    print("You chose rock \n", rock)
    print("The computer chose rock \n", rock)
    print('Is a Draw')
elif playersbet == '1' and choice == 1:
     print("You chose paper \n", paper)
     print("The computer chose paper \n", paper)
     print('Is a Draw')
elif playersbet == '2' and choice == 2:
     print("You chose scissors \n", scissors)
     print("The computer chose scissors \n", scissors)
     print('Is a Draw')
elif playersbet == '0' and choice == 1:
     print("You chose rock \n", rock)
     print("The computer chose paper \n", paper)
     print('You lose')
elif playersbet == '1' and choice == 0:
     print("You chose paper \n", paper)
     print("The computer chose rock \n", rock)
     print('You win!')
elif playersbet == '1' and choice == 2:
     print("You chose paper \n", paper)
     print("The computer chose scissors \n", scissors)
     print('You lose')
elif playersbet == '2' and choice == 1:
     print("You chose scissors \n", scissors)
     print("The computer chose paper \n", paper)
     print('You Win!')
elif playersbet == '2' and choice == 0:
     print("You chose paper \n", paper)
     print("The computer chose rock \n", rock)
     print('You Win!')
elif playersbet == '0' and choice == 2:
     print("You chose rock \n", rock)
     print("The computer chose scissors \n", scissors)
     print('You Win!')
else:
    print('Invalid Number')

# Angela's code

# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_images[user_choice])
#
#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])
#
#
#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")
