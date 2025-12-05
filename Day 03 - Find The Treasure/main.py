import art
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_story():
    clear()
    print(art.game_title)

    choice_crossroad = input("\nYou're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
    if choice_crossroad == "left":
        clear()
        print(art.game_title)

        choice_lake = input("\nYou've come to a lake. There's an island in the middle.\nDo you 'swim' or 'wait'?: ").lower()
        if choice_lake == "wait":
            clear()
            print(art.game_title)

            choice_door = input("\nYou arrive unharmed.\nThere is a house with 3 doors: Red, Yellow, and Blue.\nWhich colour do you choose?: ").lower()
            if choice_door == "yellow":
                clear()
                print(art.logo)
                print("\n💎 You found the treasure! You WIN! 💎\n")
            elif choice_door == "red":
                clear()
                print(art.game_over)
                print("\n🔥 You opened the fire room. Game Over.")
            elif choice_door == "blue":
                clear()
                print(art.game_over)
                print("\n🐺 The beasts devoured you. Game Over.")
            else:
                clear()
                print(art.game_over)
                print("\n🚪 That door does not exist. Game Over.")
        else:
            clear()
            print(art.game_over)
            print("\n🐍 You were attacked by a wild creature while swimming. Game Over.")
    else:
        clear()
        print(art.game_over)
        print("\n🕳 You fell into a deep hole. Game Over.")
while True:
    clear()
    print(art.game_title)
    print(art.menu_start)
    print(art.menu)

    user_choice = input("Choose your path: ").strip()

    if user_choice == "1":
        clear()
        print("\n⚔ The cursed path awaits... ⚔\n")
        game_story()
        input("\nPress ENTER to return to menu...")
    elif user_choice == "2":
        print("\n👁 The void consumes the weak... Farewell.\n")
        break
    else:
        print("\n❌ Invalid choice. Try again.\n")
        input("Press ENTER...")
