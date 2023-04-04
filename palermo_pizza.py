import datetime

sm = 9.99
med = 12.99
lg = 14.99
xl = 17.99
tax = 0.055

def main():
    items = []
    item = 1
    while True:
        item = input("Enter the size of the pizza you want to order (S, M, L, X), if you are done ordering just hit ENTER: ")
        if item == "S":
            item_var = sm
        elif item == 'M':
            item_var = med
        elif item == 'L':
            item_var = lg
        elif item == 'X':
            item_var = xl
        else:
            break
        quantity = float(input("How many of these would you like?"))
        items.append([item, item_var, quantity, item_var*quantity])
    
    print("-------------------------------------------------------------")
    print("WELCOME TO PALERMO PIZZA!!!")
    print("-------------------------------------------------------------")
    cost = 0
    for item in items:
        print("{} X {} Pizzas = ${:.2f}".format(int(quantity), item[0], item_var*quantity))
        cost += item_var*quantity
    print("\n-------------------------------------------------------------")
    print("Pizza Cost:                                  ${:.2f}".format(cost))
    print("Sales Tax:                                   ${:.2f}".format(cost*tax))
    print("Total:                                       ${:.2f}".format(cost + cost*tax))
    print("-------------------------------------------------------------")
    print("--------------------HAVE A SAUCY DAY ;D----------------------")
    print("-------------------------------------------------------------")
    print(str(datetime.datetime.now()))
    
        
main()