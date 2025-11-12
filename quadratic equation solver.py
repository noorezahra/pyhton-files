import math
while True:
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    c = int(input("enter c : "))
    dis = math.sqrt((b*b) - (4*a*c))
    positive_sol_of_x = ((-b) + dis)/(2*a)
    negative_sol_of_x = ((-b) - dis)/(2*a)
    print("The solutions are :",positive_sol_of_x,"and",negative_sol_of_x)
    next_calculation = input("do you want to perfrom another calculation (yes/no) : ")
    if next_calculation != "yes":
        break