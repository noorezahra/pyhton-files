import math
def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exponent_of_num(a,b):
    return a**b

def remainder(a,b):
    return a%b

def percentage(part,total):
    return (part/total) * 100

def floor_division(a,b):
    return a//b

def square_root(x):
    return math.sqrt(x)

def cube_of_num(x):
    return x**3

def square_of_num(x):
    return x**2

def cube_root(x):
    return math.cbrt(x)

def area_of_circle(r):
    return (22/7) *r*r

def area_of_rectangle(l,w):
    return l*w

def area_of_square(l):
    return l*l

def perimeter_of_square(l):
    return 4*l

def perimeter_of_rectangle(l,w):
    return 2*(l+w)

def zakat_calculator(property_value):
    return 2.5*(property_value/100)

def loss_calc(actualcost,sellcost):
    return sellcost - actualcost

def profit_calc(actualcost,sellcost):
    return actualcost - sellcost

def loss_percent_calc(actualcost,loss):
    return (loss/actualcost)*100 

def profit_percent_calc(actualcost,profit):
    return (profit/actualcost)*100

def ushr_calc(ushr_rate,earning_amount):
    return (ushr_rate/100) *earning_amount

def farheneit_to_celsius(farhenheit):
    return (farhenheit - 32)/1.8

def celsius_to_farhenheit(celsius):
    return (celsius*1.8) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273

def kelvin_to_celsius(kelvin):
    return kelvin - 273

def kelvin_to_farhenheit(kelvin): 
    return (1.8 * (kelvin - 273)) + 32

def farhenheit_to_kelvin(farhenheit):
    return ((farhenheit - 32)/1.8) - 273

while True:
    print("SELECT OPERATION : ")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.solve exponent of a number")
    print("6.find remainder")
    print("7.find percentage")
    print("8.floor division")
    print("9.find square root of a number")
    print("10.find cube root of a number")
    print("11.find square of a number")
    print("12.find cube of a number")
    print("13.find area of circle")
    print("14.find area of square")
    print("15.find area of rectangle")
    print("16.find perimeter of square")
    print("17.find perimeter of rectangle")
    print("18.find zakat on a property value")
    print("19.find ushr on an earning in agriculture")
    print("20.find profit on a sell")
    print("21.find loss on a sell")
    print("22.find profit percentage on a sell")
    print("23.find loss percentage on a sell")
    print("24.converter of farhenheit to celsius")
    print("25.converter of celsius to farhenheit")
    print("26.converter of celsius to kelvin")
    print("27.converter of kelvin to celsius")
    print("28.converter of kelvin to farhenheit")
    choice = int(input("choose from above : "))
    if choice == 1:
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))
        print("the sum of",num1,"and",num2,"is",(sum(num1,num2)))
    elif choice == 2:
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))
        print("the difference of",num1,"and",num2,"is",(subtract(num1,num2)))
    elif choice == 3:
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))
        print("the product of",num1,"and",num2,"is",(multiply(num1,num2)))
    elif choice == 4:
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))
        print(divide(num1,num2))
    elif choice == 5:
        x = float(input("enter the number : "))
        y = float(input("enter the exponent of the number : "))
        print(exponent_of_num(x,y))
    elif choice == 6:
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))
        print(remainder(num1,num2))
    elif choice == 7:
        part = float(input("enter the part : "))
        total = float(input("enter the total : "))
        print(percentage(part,total))
    elif choice == 8:
        num1 = float(input("enter first number for floor division : "))
        num2 = float(input("enter second number for floor division : "))
        print(floor_division(num1,num2))
    elif choice == 9:
        num = float(input("enter the number to find square root of : "))
        print(square_root(num))
    elif choice == 10:
        num = float(input("enter the number to find cube root of : "))
        print(cube_root(num))
    elif choice == 11:
        num = float(input("enter the number whose square you want to find : "))
        print(square_of_num(num))
    elif choice == 12:
        num = float(input("enter the number whose cube you want to find : "))
        print(cube_of_num(num))
    elif choice == 13:
        radius = float(input("enter the radius of circle : "))
        print(area_of_circle(radius))
    elif choice == 14:
        l = float(input("enter the length of side of square : "))
        print(area_of_square(l))
    elif choice == 15:
        l = float(input("enter the length of side of rectangle : "))
        w = float(input("enter the width of side of rectangle : "))
        print(area_of_rectangle(l,w))
    elif choice == 16:
        l = float(input("enter the length of side of square : "))
        print(perimeter_of_square(l))
    elif choice == 17:
        l = float(input("enter the length of side of square : "))
        w = float(input("enter the width of side of square : "))
        print(perimeter_of_rectangle(l,w))
    elif choice == 18:
        property_value = float(input("enter the value of property you own : "))
        print(zakat_calculator(property_value))
    elif choice == 19:
        ushr_rate = float(input("enter the ushr rate on your agriculture : "))
        earning_amount = float(input("enter the earning amount of your agriculture : "))
        print(ushr_calc(ushr_rate,earning_amount))
    elif choice == 20:
        actual_cost = float(input("enter the actual cost on which a product you have bought to sell : "))
        sell_cost = float(input("enter the selling price of your product : "))
        print(profit_calc(actual_cost,sell_cost))
    elif choice == 21:
        actual_cost = float(input("enter the actual cost on which a product you have bought to sell : "))
        sell_cost = float(input("enter the selling price of your product : "))
        print(loss_calc(actual_cost,sell_cost))
    elif choice == 22:
        actual_cost = float(input("enter the actual cost of the product : "))
        profit = float(input("enter the profit on the sell of your product : "))
        print(profit_percent_calc(actual_cost,profit))
    elif choice == 23:
        actual_cost = float(input("enter the actual cost of the product : "))
        loss = float(input("enter the loss on the sell of your product : "))
        print(loss_percent_calc(actual_cost,loss))
    elif choice == 24:
        farhenheit = float(input("enter degree farhenheit : "))
        print("celsius =",farheneit_to_celsius(farhenheit))
    elif choice == 25:
        celsius = float(input("enter degree celsius : "))
        print("farhenheit =",celsius_to_farhenheit(celsius))
    elif choice == 26:
        celsius = float(input("enter degree celsius : "))
        print("kelvin =",celsius_to_kelvin(celsius))
    elif choice == 27:
        kelvin = float(input("enter degree kelvin : "))
        print("celsius =",kelvin_to_celsius(kelvin))
    elif choice == 28:
        kelvin = float(input("enter degree kelvin : "))
        print("farhenheit =",kelvin_to_farhenheit(kelvin))
    elif choice == 29:
        farhenheit = float(input("enter degree farhenheit : "))
        print("kelvin =",farhenheit_to_kelvin(farhenheit))
    next_calculation = input("do you want to perform another calculation? (yes/no) : ")
    if next_calculation != 'yes':
        break