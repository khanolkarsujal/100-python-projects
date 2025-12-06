import art
import random
import os 

#Clear the sreecn
def clear():
    os.system('cls'if os.name =='nt'else 'clear')

#Generator the logo
def Generator_logo():
    print(art.logo)
    

#Created the varible    
numbers=[]
attempt = 0 

# funtion to create the numbers from 1 to 100
def generate_list_of_Numbers():

    for number in range(1,101):
        numbers.append(number)

# funtion to pick a random number from 1 to 100
def generator_random_number():

    random_number = random.choice(numbers)
    return random_number

# function to check whether user guess number same as random    
def check_user_guess(user_guess,random_number):
    
    if user_guess == random_number :
       return "correct"
        
    elif user_guess > random_number :
        
        return "high" 
        
    elif user_guess < random_number :
        
        return "low"
         
    else :
        return "Invail Input "
                

 
# startup game UI and preload
Generator_logo()
generate_list_of_Numbers()
random_number = generator_random_number()

game_on = True
is_vail_difficty = True


while game_on:
    
    
    
    while is_vail_difficty :
        user_difficity_choice = input("Choose 'Easy' Or 'Hard' :").lower()
        
        
        if user_difficity_choice == "easy":
            attempt = 10
            is_vail_difficty = False
            break
            
        elif user_difficity_choice == "hard":
            attempt = 5
            is_vail_difficty = False
            break
            
        else :
            print("Invail Input!")
    
    
    user_guess = int(input("\nGuess the number between 1 to 100! \n:"))
    
    
    check_user_guess(user_guess,random_number)
    result = check_user_guess(user_guess,random_number)



    if result == "correct":
        print("You Won")
        game_on = False
    elif result in ["high", "low"]:
        attempt -= 1
        print(f"{result}! You Have {attempt} Left!")


    if attempt == 0:
        print("\nYOU LOST! , You Have No Attempt Left ! \n")
        game_on = False
        
    














