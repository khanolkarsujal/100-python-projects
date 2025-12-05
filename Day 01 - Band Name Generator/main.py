import art

#logo
print(art.logo)
print(art.menu_start)

#Questions to generate Band Name
print("Welcome to the Band Name Generator\n")
user_input = input("\nwhat's name of the city you grew in ? : ").title()
user_input2 = input("\nwhat's your pet's name? : ").title()
print(art.menu_end)


#Generated Band Name
print(f"───── ⚔︎ Your Band Name Could Be ⚔︎ ─────: \n\n : ✦⚔︎⚔︎⚔︎ {user_input}.{user_input2} ⚔︎⚔︎⚔︎✦")
print(art.menu_end)
