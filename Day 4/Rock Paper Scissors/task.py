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

list_of_options = [rock, paper, scissors]

player_choice = int(input("Please select one of the options: 0-rock / 1-paper / 2-scissors: "))
computer_choice = random.randint(0,2)

if (player_choice == 2 and computer_choice == 1) or (player_choice == 1 and computer_choice == 0) or (player_choice == 0 and computer_choice == 2):
    print(f"You choose:\n{list_of_options[player_choice]}\n "
          f"Computer choice:\n{list_of_options[computer_choice]}.\nYou win!")
elif player_choice == computer_choice:
    print(f"You choose:\n{list_of_options[player_choice]}\n "
          f"Computer choice:\n{list_of_options[computer_choice]}.\nIt's a draw.")
else:
    print(f"You choose:\n{list_of_options[player_choice]}\n "
          f"Computer choice:\n{list_of_options[computer_choice]}.\nYou loose!")