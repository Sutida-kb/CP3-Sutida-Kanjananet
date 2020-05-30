usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "LoverBlackpink"  and passwordInput == "5555":
    print("==================================")
    print("Wellcome to BLACKPINK Lover shop^^")
    print("----------------------------------")
    print("Promotion Sale for this week!!")
    print("         ")
    print("1) Blackpink Photobook                        ","   900THB")
    print("2) Blackpink in Your AREA album               ","  1200THB")
    print("3) Case Airpods BP limited edition            ","   900THB")
    print("4) T-shirt BP in Hawaii                       ","   700THB")
    print("5) Grip Holder special edition                ","  2000THB")
    print("         ")
    selectnumber=int(input("Please select tne number to Add the cart(1-5) >>"))
    if selectnumber == 1:
        print("How many item do you need?")
        BpPhotobookCount=int(input("Blackpink Photobook:"))
        print("total amount:",BpPhotobookCount*900,"THB")
    elif selectnumber ==2:
        print("How many item do you need?")
        BpAlbumCount=int(input("Blackpink in Your AREA album:" ))
        print("total amount:", BpAlbumCount * 1200, "THB")
    elif selectnumber == 3:
        print("How many item do you need?")
        CaseAirpodCount = int(input("Case Airpods BP limited edition:"))
        print("total amount:", CaseAirpodCount * 900, "THB")
    elif selectnumber == 4:
        print("How many item do you need?")
        TshirtCount = int(input("T-shirt BP in Hawaii:"))
        print("total amount:", TshirtCount * 700, "THB")
    elif selectnumber == 5:
        print("How many item do you need?")
        GripHolderCount = int(input("Grip Holder special edition:"))
        print("total amount:", GripHolderCount * 2000, "THB")

print("------------thank you ---------------")
