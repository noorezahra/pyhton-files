import math
while True:
    a = float(input("enter the length of first side of triangle:"))
    b = float(input("enter the length of second side of triangle:"))
    c = float(input("enter the length of third side of triangle:"))
    s = (a + b + c)/ 2
    number = (s * (s - a) * (s - b) * (s - c))
    area = math.sqrt(number)
    print("the area of triangle is", area)
    next_calculation = input("do you want to perform another calculation? (yes/no) : ")
    if next_calculation != 'yes':
        break