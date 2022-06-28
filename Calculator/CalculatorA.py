import os
from CalcArt import logo
#print(logo)


def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# os.system('clear')
# num1 = int(input("First number: "))
#num2 = int(input("Second number: "))

cho = ""


# print(operations)

def calcul(): # RECURSION
    os.system('clear')
    print(logo)
    #os.system('clear')
    num1 = float(input("First number: "))

    for opr in operations:
        print(f'{opr} ')
    

    cont = True

    while  cont:
        # for opr in operations:
        #  print(f'{opr} ')

        oper = input("Select an operation: ")
        num2 = float(input("Next number: "))

        calc_fun = operations[oper]  # HERE WE ACCESS THE FUNCTIONS ABOVE VIA THE "the DICTIONARY 'VALUE'  "
                                     # 'DICTIONARY' DATA FRAME OR TYPE OR WHATEVER
        print(f'\n Operacion: {calc_fun} \n')
        result1 = (calc_fun(num1, num2))
        print(f"{num1} {oper} {num2} = Result 1: {result1}")

        # oper = input("Select another operation: ")
        # num3 = int(input("Next number: "))
        # calc_fun = operations[oper]
        # result2 = (calc_fun(result1, num3))
        

        if input(f"Continue with {result1} type 'y' or 'n' to start a new calculation ") == "y":
            num1 = result1
        else:
            cont = False
            os.system('clear')
            calcul()

#print(f"1st Result: {result1} {oper} {num3} =  2nd Result: {result2}")

calcul()

# for opr in operations:
#     print(f'{opr} ')

#   sel = input("Select an operator: ")

#   #print(f'\n {opr} ')

#   if sel == "+":
#     print(f'Additon result: {num1} {sel} {num2} = {add(num1, num2)}')
#   elif sel == "n":
#     break

#   if sel == "-":
#     print(f'Substracton result: {num1} {sel} {num2} = {sub(num1, num2)}')
#   elif sel == "n":
#     break

#   if sel == "*":
#     print(f'Multiplication result: {num1} {sel} {num2} = {mul(num1, num2)}')
#   elif sel == "n":
#     break

#   if sel == "/":
#     print(f'Division result: {num1} {sel} {num2} = {div(num1, num2)}')
#   elif sel == "n":
#     break