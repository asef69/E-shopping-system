from abc import ABC
from products import Product
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.orders = []

    def view_products(self, store):
        print("\nAvailable Products:")
        available = False
        for product in store.products:
            if product.stock > 0:
                print(f"- {product.name} | ${product.price} | Stock: {product.stock}")
                available = True
        if not available:
            print("No products available at the moment.")

    def place_order(self, store):
        product_name = input("Enter the product name you want to order: ")
        quantity = int(input("Enter quantity: "))
        for product in store.products:
            if product.name.lower() == product_name.lower() and product.stock >= quantity:
                product.stock -= quantity
                self.orders.append((product, quantity))
                print(f"✅ Order placed for {quantity} x {product.name}")
                return
        print("❌ Product not available or insufficient stock.")


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def publish_product(self, store):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
        product = Product(name, price, stock, self)
        self.products.append(product)
        store.products.append(product)
        print(f"✅ Product '{name}' added with stock {stock}.")







