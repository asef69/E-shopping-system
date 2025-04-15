from products import Product
from users import User,Seller,Customer
from store import Store
def main():
    store = Store()

    while True:
        print("\n--- E-Shopping App ---")
        print("1. Register as Customer")
        print("2. Register as Seller")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            customer = store.register_customer()
            while True:
                print("\n1. View Products")
                print("2. Place Order")
                print("3. Logout")
                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    customer.view_products(store)
                elif sub_choice == "2":
                    customer.view_products(store)
                    customer.place_order(store)
                elif sub_choice == "3":
                    break
                else:
                    print("❌ Invalid option")

        elif choice == "2":
            seller = store.register_seller()
            while True:
                print("\n1. Add Product")
                print("2. Logout")
                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    seller.publish_product(store)
                elif sub_choice == "2":
                    break
                else:
                    print("❌ Invalid option")

        elif choice == "3":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
