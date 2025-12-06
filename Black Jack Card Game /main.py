import art 
import random
import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(art.logo)

Deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10]

def draw_card():
    return random.choice(Deck_of_cards)    

def draw_random_two_cards():
    return [draw_card(), draw_card()]
    
user_cards = draw_random_two_cards()
computer_cards = draw_random_two_cards()

print(f"You: {user_cards[0]} , {user_cards[1]} = {sum(user_cards)} ")
print(f"Dealer (Computer): {computer_cards[0]} , ❓ \n")

def hit():
    user_cards.append(draw_card())

def stand():
    while sum(computer_cards) < 17:
        computer_cards.append(draw_card())

def playerscore():
    print(f"\nYour hand: {user_cards} (Total: {sum(user_cards)})")
    print(f"Dealer's hand: {computer_cards} (Total: {sum(computer_cards)})")


while True:
    user_current_score = sum(user_cards)
    computer_current_score = sum(computer_cards)

    if user_current_score == 21:
        playerscore()
        print("You Win And It's Blackjack!")
        break

    user_choice = input("You choose:\nHit → take another card \nStand → stop taking cards\n: ").lower()

    if user_choice == "hit":
        hit()

    elif user_choice == "stand":
        stand()
    else:
        print("Invalid Input!")
        continue

    clear()
    print(art.logo)

    user_current_score = sum(user_cards)
    computer_current_score = sum(computer_cards)

    # Bust conditions
    if user_current_score > 21:
        playerscore()
        print("You Lost!")
        break
    if computer_current_score > 21:
        playerscore()
        print("You Win!")
        break

    # If user stands, game must compare scores
    if user_choice == "stand":
        playerscore()
        if user_current_score == computer_current_score:
            print("It's A Draw!")
        elif computer_current_score > user_current_score:
            print("You Lost!")
        else:
            print("You Win!")
        break
