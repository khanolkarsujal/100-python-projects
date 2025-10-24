print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill?\n"))
spilt_bill = float(input("How many people to split the bill?\n"))
tip = float(input("What percentage tip would you like to give? 10 , 12 , or 15 ? \n"))
                    
spilt_amount = float(bill_amount/spilt_bill)
tip_percetage_amount = spilt_amount*(tip/100)
final_amount = spilt_amount + tip_percetage_amount
print(f"Each person should pay:${final_amount}")


