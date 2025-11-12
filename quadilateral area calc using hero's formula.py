import math
while True:
    perp1 = float(input("enter the length of perp1 of quadilateral : "))
    base1 = float(input("enter the length of base1 of quadilateral : "))
    perp2 = float(input("enter the length of perp2 of quadilateral : "))
    base2 = float(input("enter the length of base2 of quadilateral : "))
    diagonal = float(input("enter the length of diagonal of quadilateral : "))
    s1 = (perp1+base1+diagonal)/2
    s2 = (perp2+base2+diagonal)/2
    area_1 = s1*(s1-perp1)*(s1-base1)*(s1-diagonal)
    area1 = math.sqrt(area_1)
    area_2 = s2*(s2-perp2)*(s2-base2)*(s2-diagonal)
    area2 = math.sqrt(area_2)
    total_area = area1 + area2
    print("the area of quadilateral =",total_area)
    next = input("do you want to do another calculation (yes/no) : ")
    if next != "yes":
        break