import subprocess
import csv

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


def update_product_price(product_id, new_price):
    """
    Updates the price of an existing product in inventory (products.csv).
    """
    products = read_products()
    found = False
    for product in products:
        if product["id"] == product_id:
            found = True
            product["price"] = str(new_price)  # Update price
            break
    if found:
        write_products(products)  # Write changes to products.csv
        print(f"Price of product {product_id} updated successfully!")
        subprocess.run(['git', 'commit', '-m', f"Updated price of product: {product_id}"])  # Git commit
    else:
        print(f"Product {product_id} not found in inventory.") 

def write_products(products):
  """
  Writes product data to products.csv from a list of dictionaries.
  """
  with open("products.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "price", "quantity"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)


def restock_product(product_id, quantity):
  """
  Updates the quantity of an existing product in inventory (products.csv).
  """
  products = read_products()
  found = False
  for product in products:
    if product["id"] == product_id:
      found = True
      product["quantity"] = str(int(product["quantity"]) + quantity)  # Update quantity
      break
  if found:
    write_products(products)  # Write changes to products.csv
    print(f"Product {product_id} restocked successfully!")
    subprocess.run(['git', 'commit', '-m', f"Restocked product: {product_id}"])  # Git commit
  else:
    print(f"Product {product_id} not found in inventory.")


def add_product(product_id, name, price, quantity):
  """
  Adds a new product to the inventory (products.csv).
  """
  products = read_products()
  for product in products:
    if product["id"] == product_id:
      print(f"Product with ID {product_id} already exists.")
      return
  products.append({
      "id": product_id,
      "name": name,
      "price": price,
      "quantity": str(quantity)  # Convert quantity to string for CSV writing
  })
  write_products(products)
  print(f"Product {name} added successfully!")
  subprocess.run(['git', 'commit', '-m', f"Added new product: {name}"])

def seller_menu():
    """
    Menu for seller/admin options.
    """
    while True:
        print("\nSeller Menu")
        print("1. View Products")
        print("2. Restock Product")
        print("3. Update Product Price")
        print("4. Add New Product")
        print("5. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            product_id = input("Enter product ID to restock: ")
            quantity = int(input("Enter quantity to add: "))
            restock_product(product_id, quantity)
        elif choice == "3":
            product_id = input("Enter product ID to update price: ")
            new_price = float(input("Enter new price: "))
            update_product_price(product_id, new_price)
        elif choice == "4":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(product_id, name, price, quantity)
        elif choice == "5":
            print("Exiting to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")