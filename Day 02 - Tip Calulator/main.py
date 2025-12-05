import art

#logo Tip Calulator
print(art.logo)
print(art.menu_start)

print("Welcome To The Tip Calculator.")

#Taking inputs
bill_amount = float(input("What Was The Total Bill? :$"))
number_of_people = float(input("\nHow Many People To Split The Bill? :"))
tip_percetage = float(input("\nWhat Percentage(%) Tip Would You Like To Give? 10 , 12 , or 15 ? :%"))

#Calulations                   
amount_per_person_before_tip = float(bill_amount/number_of_people)
tip_per_person = number_of_people*(amount_per_person_before_tip/100)
final_amount_per_person = amount_per_person_before_tip + tip_per_person

print(art.menu_end) 

print(f"───── ⚔︎  Each Person Should Pay ⚔︎ ───── \n\n : ───── ${final_amount_per_person} ───── ")
print(art.menu_end)


