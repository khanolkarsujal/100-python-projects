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

game_images = [rock, paper, scissors]


#user choice
user_choice = input("what do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors :")

if user_choice in ["0","1","2"]:
    user_index = int(user_choice)
    print("YOU HAVE CHOOSE:\n",game_images[user_index])
else:
    print("YOU HAVE CHOOSE OPTION THAT DOESN'T EXIST ")
    exit()


#computer choice

comp_choice = random.choice(game_images)
comp_index = game_images.index(comp_choice)
print(f"\nCOMPUTER CHOOSE:\n{comp_choice}")

#draw
if user_index == comp_index : 
    print("It is a draw, a tie") 
#for rock
elif user_index == 0 and comp_index ==1 :
    print("YOU LOST !")
elif user_index == 0 and comp_index ==2 :
    print("YOU WON !")
#for paper
elif user_index == 1 and comp_index ==2 :
    print("YOU LOST !")
elif user_index == 1 and comp_index ==0 :
    print("YOU WON !")  
#for scissors
elif user_index == 2 and comp_index ==0 :
    print("YOU LOST !")
elif user_index == 2 and comp_index ==1 :
    print("YOU WON !")








