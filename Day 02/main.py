import art

#logo Tip Calulator
print(art.logo)
print(art.menu_start)

print("Welcome to the tip calculator.")

#Taking inputs
bill_amount = float(input("What was the total bill? :"))
spilt_bill = float(input("\nHow many people to split the bill? :"))
tip = float(input("\nWhat percentage tip would you like to give? 10 , 12 , or 15 ? :"))

#Calulations                   
spilt_amount = float(bill_amount/spilt_bill)
tip_percetage_amount = spilt_amount*(tip/100)
final_amount = spilt_amount + tip_percetage_amount

print(art.menu_end) 

print(f"───── ⚔︎  Each person should pay ⚔︎ ───── \n : ${final_amount} ")
print(art.menu_end)


