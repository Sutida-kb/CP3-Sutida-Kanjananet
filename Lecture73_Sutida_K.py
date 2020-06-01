systemMenu = {"ข้าวมันไก่":40,"ข้าวหมูแดง":45,"ข้าวขาหมู":50,"ข้าวหมูกรอบ":35}
menuList = []
def showBill():
    totalPrice = 0
    print("My food".center(17,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
        result = totalPrice+ totalPrice * 7 / 100
    print("Total cost:",totalPrice, "THB")
    print("Total cost+vat:",result,"THB")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
print("Thank you".center(17,"-"))