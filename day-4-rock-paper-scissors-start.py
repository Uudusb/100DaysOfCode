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

import random

myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

hand = [rock, paper, scissors]
print(f"You chose:\n{hand[myChoice]}")

computerChoice = random.randint(0, 2)
print(f"Computer chose:\n{hand[computerChoice]}")

if myChoice == computerChoice:
  print("Tied.")
else:
  if myChoice < computerChoice:
    if myChoice == 0 and computerChoice == 2:
      print("You won.")
    else:
      print("You lose.")
  else:
    if myChoice == 2 and computerChoice == 0:
      print("You lose.")
    else:
      print("You won.")
