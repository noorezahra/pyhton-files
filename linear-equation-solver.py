while True:
    variable = input("enter the variable : ")
    coeffecient = int(input("enter the coeffecient of variable : "))
    constant_on_lhs = int(input("enter the constant on LHS of equation : "))
    constant_on_rhs = int(input("enter the constant on RHS of equation : "))
    sol_part1 = constant_on_rhs - constant_on_lhs
    sol = sol_part1/coeffecient
    print("the solution of",variable,":",sol)
    next_calc = input("do you want to perform another calculation (yes/no) : ")
    if next_calc != "yes":
        break