def vatCalculator(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result

cost=int(input("TotalPrice:"))
print(vatCalculator(cost))