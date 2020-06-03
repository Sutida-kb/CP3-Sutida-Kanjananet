class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart (self):
        print("Added this product to", self.name, self.lastname, "'s cart.")

customer1 = Customer()
customer1.name = "Lisa"
customer1.lastname = "Blackpink"
customer1.addCart()

customer2 = Customer()
customer2.name = "Jennie"
customer2.lastname = "Blackpink"
customer2.addCart()

customer3 = Customer()
customer3.name = "Rose"
customer3.lastname = "Blackpink"
customer3.addCart()

customer4 = Customer()
customer4.name = "Jisoo"
customer4.lastname = "Blackpink"
customer4.addCart()