import subprocess
import csv
import datetime

def read_products():
  """
  Reads product data from products.csv and returns a list of dictionaries.
  """
  products = []
  try:
    with open("products.csv", "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        products.append(row)
  except FileNotFoundError:
    print("Error: products.csv file not found.")
  return products

def write_products(products):
  """
  Writes product data to products.csv from a list of dictionaries.
  """
  with open("products.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "price", "quantity"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

def view_products():
    """
    Displays a list of all products with their details.
    """
    products = read_products()
    if not products:
        print("No products found in inventory.")
        return

    print("\nProducts:")
    print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Name", "Price", "Quantity"))
    print("-" * 60)
    for product in products:
        print("{:<10} {:<20} ${:<10.2f} {:<10}".format(product["id"], product["name"], float(product["price"]), product["quantity"]))

def purchase_product(product_id, quantity):
  """
  Handles product purchase, updating inventory, purchase history, and providing bill details.
  """
  products = read_products()
  found = False
  total_cost = 0.0  # Initialize total_cost outside the loop

  for product in products:
    if product["id"] == product_id:
      if int(product["quantity"]) >= quantity:
        total_cost = float(product["price"]) * quantity
        print(f"This will cost you ${total_cost:.2f} for {product['name']} x {quantity}. Confirm purchase? (y/n): ".lower())
        confirmation = input().lower()
        if confirmation == 'y':
          product["quantity"] = str(int(product["quantity"]) - quantity)
          found = True
          print("Purchase successful!")
          timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          with open("purchase_history.txt", "a") as file:
            file.write(f"{timestamp}|{product_id}|{quantity}\n")  # Write to history only on confirmed purchase
          subprocess.run(['git', 'commit', '-m', f"Purchase of product: {product_id}"])  # Git commit for confirmed purchase only
          write_products(products)  # Write changes to products.csv only on confirmed purchase
          break
        else:
          print("Purchase cancelled.")
          break
      else:
        print(f"Product {product_id} is out of stock or quantity entered is invalid.")
        break

  if not found:
    print(f"Product {product_id} not found in inventory.")


def buyer_menu():
    """
    Menu for buyer/customer options.
    """
    while True:
        print("\nBuyer Menu")
        print("1. View Products")
        print("2. Purchase Product")
        print("3. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            purchase_product(product_id, quantity)
        elif choice == "3":
            print("Exiting to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

