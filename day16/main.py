from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menuItem = MenuItem()
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()



is_on = True

while is_on:
    while True:
     order =input(f"Choose from options {menu.get_items() :}")
     
     
     if order == "off":
      is_on = False  
     elif order == "report":
       coffeeMaker.report()
       
     else :
       order_name = menu.find_drink(order)
       check_resource = coffeeMaker.is_resource_sufficient(order_name)
       if check_resource == True :
        # print(f"check resource :{check_resource}")
        if order_name != "None" :
         
         money = moneyMachine.make_payment(order_name.cost)

         if money:
          coffeeMaker.make_coffee(order_name)
         

             
       


      
