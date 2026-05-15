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

# Method - 1
game_images = [rock, paper, scissors]

computer = random.randint(0, 2)

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >= 0 and user <= 2:
     print(game_images[user])
     print("Computer Choose: ")
     print(game_images[computer])


if user < 0 or user > 2:
    print("Invalid Choice! Please enter number correctly")
elif user == 0 and computer == 1:
    print("You lose!")
elif user == 1 and computer == 2:
    print("You lose!")
elif user == 2 and computer == 1:
    print("You Win!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user == 1 and computer == 0:
    print("You Win!")
elif user == 0 and computer == 2:
    print("You Win!")
# elif user == computer:
#     print("It's a draw")
else:
    print("It's a draw")


# Method - 2
# if user < 0 or user > 2:
#     print("Invalid Choice! Please enter number correctly")
# else:
#     print(game_images[user])
#     print("Computer Choose: ")
#     print(game_images[computer])
#
#
#     if (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
#         print("You Win!")
#     elif user == computer:
#         print("It's a draw")
#     else:
#         print("You lose")



# Method - 3
# game_image = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# computer_choice = random.randint(0, 2)
# if user_choice >= 0 and user_choice <=2:
#     print(game_image[user_choice])
#     print("Computer Choice: ")
#     print(game_image[computer_choice])
#
# if user_choice >= 3 or user_choice < 0:
#     print("Invalid Choice! Please enter number correctly ")
# elif user_choice == 0 and computer_choice == 2:
#     print("You Win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You Win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")