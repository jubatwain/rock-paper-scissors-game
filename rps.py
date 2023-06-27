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
---'   ____)_______
          _________)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
value = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
if value == 0:
  print(rock)
elif value == 1:
  print(paper)
elif value == 2:
  print(scissors)

comp_choice = random.randint(0, 2)
print("Computer chose: ")
if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
elif comp_choice == 2:
  print(scissors)

# rock wins against scissors
# scissors win against paper
# paper wins against rock
if value == comp_choice:
  print("It's a draw.")
elif value == 0 and comp_choice == 2: #rock against scissors
  print("You win! for once 😅")
elif value == 0 and comp_choice == 1: #rock against paper
  print("You lose! You're miserable, pathetic even.")
elif value == 1 and comp_choice == 2: #paper against scissors
  print("You lose. Ik it sucks but it's not the end of the world.")
elif value == 1 and comp_choice == 0: #paper against rock
  print("You win. Don't hype yourself up, you just got lucky.")
elif value == 2 and comp_choice == 1: #scissors against paper
  print("You win!")
elif value == 2 and comp_choice == 0: #scissors against rock
  print("You lose, again!")
