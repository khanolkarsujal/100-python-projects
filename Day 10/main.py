

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

number1 = int(input("what`s the first number : "))
number2 = int(input("what`s the second number : "))

for symbols in opertions :
    print(symbols)
opertions_symbols = input("Pick an operation from line above : ")    

result = opertions[opertions_symbols](number1, number2)




print(f"{number1} {opertions_symbols} {number2} = {result}")