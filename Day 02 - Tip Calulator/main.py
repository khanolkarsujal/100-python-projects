import art

#logo Tip Calulator
print(art.logo)
print(art.menu_start)

print("Welcome To The Tip Calculator.")

#Taking inputs
bill_amount = float(input("What Was The Total Bill? :$"))
spilt_bill = float(input("\nHow Many People To Split The Bill? :"))
tip = float(input("\nWhat Percentage(%) Tip Would You Like To Give? 10 , 12 , or 15 ? :%"))

#Calulations                   
spilt_amount = float(bill_amount/spilt_bill)
tip_percetage_amount = spilt_amount*(tip/100)
final_amount = spilt_amount + tip_percetage_amount

print(art.menu_end) 

print(f"───── ⚔︎  Each Person Should Pay ⚔︎ ───── \n\n : ───── ${final_amount} ───── ")
print(art.menu_end)


