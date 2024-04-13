from Shopkeeper import seller_menu as Shopkeeper
from Customer import buyer_menu as Customer

def main():
    """
    Main program loop for user interaction.
    """
    while True:
        print("\nWelcome to our Inventory Management System!")
        print("Are you a Buyer or Seller?")
        print("1. Buyer")
        print("2. Seller")
        print("3. Exit")
        user_type = input("Enter your choice: ")

        if user_type == "1":  # Buyer
            Customer()
        elif user_type == "2":  # Seller
            Shopkeeper()
        elif user_type == "3":  # Exit
            print("Thanks for shopping with us!")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")


if __name__ == "__main__":
    main()
