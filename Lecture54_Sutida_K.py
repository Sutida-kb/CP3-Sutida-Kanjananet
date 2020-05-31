def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    elif usernameInput != "admin" or passwordInput != "1234":
        print("ID username or password not correct!!")
        return login()
def showMenu() :
    print("----*---- ChillChillShop ----*----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return select()
def select() :
    Select = int(input("Select >> "))
    if Select == 1:
        return vatCalculate(int(input("totalprice >> ")))
    elif Select == 2:
        return priceCalculate()
def vatCalculate(totalprice) :
    vat = 7
    result = totalprice+(totalprice*7/100)
    return print("Exclude VAT",result, "THB")
def priceCalculate() :
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)


print(login())
print("-------Thank you-------")