def register():
  print("Welcome to the registration page of ShRaya And The Last Dragon :)")
  name = input("Enter your name: ")
  phone = input("Enter your phone number: ")
  address = input("Enter your address: ")
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  print("Registration successful")
  print("You are now logged in")
  print("------------------------\n")


  return name, phone, address, username, password

def display_categories():
  print("Choose the category you want to shop from: ")
  print("1.Food")
  print("2.Groceries")
  print("3.Health & Beauty")
  print("4.Medicine")
  category = int(input("Enter the category number (1-4): "))
  while category < 1 or category > 4:
    print("Invalid category number")
    category = int(input("Enter the category number: "))
  return category

food_shops = ["El-Abd", "Burger King", "El-Dahhan"]
groceries_shops = ["Metro", "Seoudi", "El-Mahallawy"]
health_beauty_shops = ["Infinity", "Raw African", "Azha"]
medicine_shops = ["El-Ezaby", "Seif", "19011"]

def display_restaurants_shops(category):
  print("Choose the shop you want to shop from: ")
  shops = []
  if category == 1:
    for i in range(len(food_shops)):
      print(i+1, food_shops[i])
    shops  = food_shops
  elif category == 2:
    for i in range(len(groceries_shops)):
      print(i+1, groceries_shops[i])
    shops = groceries_shops
  elif category == 3:
    for i in range(len(health_beauty_shops)):
      print(i+1, health_beauty_shops[i])
    shops = health_beauty_shops
  elif category == 4:
    for i in range(len(medicine_shops)):
      print(i+1, medicine_shops[i])
    shops = medicine_shops

  shop = int(input("Enter the shop number: "))
  return shops[shop-1]

el_abd_menu = ["Ice Cream", "Cake", "Cookies"]
el_abd_prices = [10, 20, 30]
burger_king_menu = ["Burger", "Fries", "Nuggets"]
burger_king_prices = [40, 30, 20]
el_dahhan_menu = ["Kebab", "Kofta", "Grilled Chicken"]
el_dahhan_prices = [50, 60, 70]

metro_menu = ["Milk", "Eggs", "Bread"]
metro_prices = [5, 10, 15]
seoudi_menu = ["Rice", "Pasta", "Sugar"]
seoudi_prices = [20, 25, 30]
el_mahallawy_menu = ["Oil", "Salt", "Pepper"]
el_mahallawy_prices = [35, 40, 45]

infinity_menu = ["Shampoo", "Conditioner", "Body Lotion"]
infinity_prices = [50, 60, 70]
raw_african_menu = ["Hair Gel", "Hair Spray", "Hair Cream"]
raw_african_prices = [80, 90, 100]
azha_menu = ["Face Cream", "Face Wash", "Face Toner"]
azha_prices = [110, 120, 130]

el_ezaby_menu = ["Panadol", "Aspirin", "Cough Syrup"]
el_ezaby_prices = [140, 150, 160]
seif_menu = ["Bandages", "Disinfectant", "Plaster"]
seif_prices = [170, 180, 190]
nineteen_menu = ["Thermometer", "Blood Pressure Monitor", "Glucose Monitor"]
nineteen_prices = [200, 210, 220]

def display_menu(shop):
  print("Choose the item you want to buy: ")
  items = []
  prices = []
  if shop == "El-Abd":
    for i in range(len(el_abd_menu)):
      print(i+1, el_abd_menu[i])
    items = el_abd_menu
    prices = el_abd_prices
  elif shop == "Burger King":
    for i in range(len(burger_king_menu)):
      print(i+1, burger_king_menu[i])
    items = burger_king_menu
    prices = burger_king_prices
  elif shop == "El-Dahhan":
    for i in range(len(el_dahhan_menu)):
      print(i+1, el_dahhan_menu[i])
    items = el_dahhan_menu
    prices = el_dahhan_prices

  elif shop == "Metro":
    for i in range(len(metro_menu)):
      print(i+1, metro_menu[i])
    items = metro_menu
    prices = metro_prices
  elif shop == "Seoudi":
    for i in range(len(seoudi_menu)):
      print(i+1, seoudi_menu[i])
    items = seoudi_menu
    prices = seoudi_prices
  elif shop == "El-Mahallawy":
    for i in range(len(el_mahallawy_menu)):
      print(i+1, el_mahallawy_menu[i])
    items = el_mahallawy_menu
    prices = el_mahallawy_prices

  elif shop == "Infinity":
    for i in range(len(infinity_menu)):
      print(i+1, infinity_menu[i])
    items = infinity_menu
    prices = infinity_prices
  elif shop == "Raw African":
    for i in range(len(raw_african_menu)):
      print(i+1, raw_african_menu[i])
    items = raw_african_menu
    prices = raw_african_prices
  elif shop == "Azha":
    for i in range(len(azha_menu)):
      print(i+1, azha_menu[i])
    items = azha_menu
    prices = azha_prices

  elif shop == "El-Ezaby":
    for i in range(len(el_ezaby_menu)):
      print(i+1, el_ezaby_menu[i])
    items = el_ezaby_menu
    prices = el_ezaby_prices
  elif shop == "Seif":
    for i in range(len(seif_menu)):
      print(i+1, seif_menu[i])
    items = seif_menu
    prices = seif_prices
  elif shop == "19011":
    for i in range(len(nineteen_menu)):
      print(i+1, nineteen_menu[i])
    items = nineteen_menu
    prices = nineteen_prices

  item_number = int(input("Enter the item number (1-3): "))
  while item_number < 1 or item_number > 3:
    print("Invalid item number")
    item_number = int(input("Enter the item number (1-3): "))
  quantity = int(input("Enter the quantity (1, 2, 3, 4, ....): "))

  add_to_cart(items[item_number-1], prices[item_number-1], quantity)

  another_order = input("Do you want to add another item? (1. Yes, 2. No): ")
  if another_order == "1":
    display_menu(shop)

def add_to_cart(item, price, quantity):
  cart.append(item)
  prices.append(price * quantity)
  print("Item added to cart")

def view_remove_cart(cart, prices):
  print("Items in cart: ")
  for i in range(len(cart)):
    print(i+1, cart[i])
  remove = input("Do you want to remove any item from cart? (1. Yes, 2. No): ")
  if remove == "1":
    item_number = int(input("Enter the item number you want to remove: "))
    cart.pop(item_number-1)
    prices.pop(item_number-1)
    print("Item removed from cart")

def checkout(cart):
  print("Checking out")
  print("Delivery Information: ")
  print("Address: ", address)
  print("Phone: ", phone)
  print("Items in cart: ")
  for i in range(len(cart)):
    print('-', cart[i], prices[i])
  
  payment_method = input("Enter payment method (1. Visa, 2. Cash): ")
  if payment_method == "1":
    payment_method = "Visa"
  elif payment_method == "2":
    payment_method = "Cash"
  return payment_method

def place_order(cart, prices):
  print("Order placed")
  print("Restaurant/Shop: ", shop)
  print("Date: ", "21/12/2024")
  print("Order No. ", "1234")
  print("Delivery Information: ")
  print("Address: ", address)
  print("Phone: ", phone)
  print("Items in cart: ")
  total = 0
  for i in range(len(cart)):
    print('-', cart[i],  prices[i])
    total += prices[i]
  print("Order Subtotal: ", total)
  print("Delivery Fee: ", 10)
  print("Service Fee: ", 5)
  print("Total: ", total+10+5)
  print("Payment Method: ", payment_method)
  print("Thank you for shopping with us")
  

cart = []
prices = []

while True:
  name, phone, address, username, password = register()
 

  category = display_categories()
  print("------------------------\n")
  shop = display_restaurants_shops(category)
  print("------------------------\n")
  display_menu(shop)
  print("------------------------\n")
  view_remove_cart(cart, prices)
  print("------------------------\n")
  payment_method = checkout(cart)
  print("------------------------\n")
  place_order(cart, prices)
  print("------------------------\n")
  end = input("Do you want to end the program? (1. Yes, 2. No): ")
  if end == "1":
    break

