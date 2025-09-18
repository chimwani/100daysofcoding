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
game_images=[rock,paper,scissors]
# 0for rock 1 for paper and 2 for scissors.
user_choice = int(input("whats your choice ? \nType 0for rock 1 for paper and 2 for scissors.\n"))
computer_choice = random.randint(0 ,2 )

print (f"the computer chose {computer_choice}")
print(game_images[computer_choice])

print(f" you chose {user_choice}")
if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])
if user_choice >=3 or user_choice < 0:
    print("invalid choice. you loose!")

if computer_choice == 0 and user_choice ==2:
    print("you loose!")
elif computer_choice > user_choice:
    print("you loose!")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice>computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its a draw")