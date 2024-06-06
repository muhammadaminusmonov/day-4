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

chosen_one = int(input("enter 0 for rock, 1 for paper, 2 for scissors: "))
if 0 <= chosen_one <= 2:
    list_choices = [rock, paper, scissors]
    pc_choice = random.randint(0, len(list_choices) - 1)
    print(f"Your choice is\n{list_choices[chosen_one]}")
    print(f"Computer's choice is\n{list_choices[pc_choice]}")
    if (chosen_one - pc_choice) == 1 or (chosen_one - pc_choice) == -2:
        print("You won")
    elif chosen_one == pc_choice:
        print("Draw")

    else:
        print("You lost")
else:
    print("You entered wrong number.")
