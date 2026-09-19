menue ={
    "Dosa":60,
    "Tea":12,
    "Idli":20,
    "Vada":20,
    "Upma":35

}

print("Welcome To RR Restaurant")
print("Dosa: 60\nTea: 12\nIdli: 20\nVada: 20\nUpma: 35")

Bill=0
while True:
    order = input("Enter your order or d to end:")
    if order == "d":
        break
    elif order in menue:
        quantity = int(input("Enter quantity: "))
        Bill =Bill+(menue[order]*quantity)
    else:
        print("This item is not available")

print("Your Bill= ",Bill)
print("GST=",(18/100))
print("Total=",Bill+(18/100)*Bill)