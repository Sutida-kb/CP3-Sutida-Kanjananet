menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("My food".center(17,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
        result = totalPrice+ totalPrice * 7 / 100
    print("Total cost:",totalPrice, "THB")
    print("Total cost+vat:",result,"THB")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)


showBill()
print("Thank you".center(17,"-"))