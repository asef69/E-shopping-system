from users import User,Seller,Customer
class Store:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def register_customer(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        customer = Customer(email, password)
        self.customers.append(customer)
        print(f"✅ Customer account created for {email}")
        return customer

    def register_seller(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        seller = Seller(email, password)
        self.sellers.append(seller)
        print(f"✅ Seller account created for {email}")
        return seller
