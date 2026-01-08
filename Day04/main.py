import random
rock = '''
    _______
---'   ____)
      (_____)
Rock  (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
Paper     _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
Scissors  ______)
       __________)
      (____)
---.__(___)
'''
game_ascii = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice >= 3 :
    print("You typed and invalid number, you lose!")
else:
    user_img = game_ascii[user_choice]
    computer_img = game_ascii[computer_choice]

    print(f"You chose:\n{user_img}")
    print(f"Computer chose:\n{computer_img}")

    if user_choice == computer_choice:
        print("It is a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win")
    else:
        print("You lose!")

