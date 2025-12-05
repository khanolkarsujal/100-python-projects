import art

#calulator

#Addition
def addition(number1 , number2):
    return number1 + number2

#Subtraction
def subtraction(number1 , number2):
    return number1 - number2

#Multiplcation
def multplication (number1 , number2):
    return number1 * number2

#Division
def division (number1 , number2):
    return number1 / number2

opertions = {
    "+": addition ,
    "-": subtraction ,
    "*": multplication ,
    "/": division,
}
calulator_on = True

#logo
calulator_logo = art.logo
print(calulator_logo)


number1 = int(input("what`s the first number : "))

while calulator_on :
    

    for symbols in opertions :
        print(symbols)
    opertions_symbols = input("Pick an operation from line above : ")    

    number2 = int(input("what`s the second number : "))

    result = opertions[opertions_symbols](number1, number2)

    print(f"{number1} {opertions_symbols} {number2} = {result}")

    number1 = result

    user_chocie = input("Type 'y' to continue to calulate or 'n' to exit : ").lower()

    if user_chocie == "y":
         continue
         
    elif user_chocie == "n":
        calulator_on = False

    else:
            print("Invaid input ! ")



