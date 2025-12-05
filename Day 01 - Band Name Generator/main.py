import art

#logo
print(art.logo)
print(art.menu_start)

#Questions to generate Band Name
print("Welcome To The Band Name Generator\n")
user_input = input("\nWhat's Name Of The City You Grew In ? : ").title()
user_input2 = input("\nWhat's Your Pet's Name? : ").title()
print(art.menu_end)


#Generated Band Name
print(f"───── ⚔︎ Your Band Name Could Be ⚔︎ ─────: \n\n : ✦⚔︎⚔︎⚔︎ {user_input}.{user_input2} ⚔︎⚔︎⚔︎✦")
print(art.menu_end)
