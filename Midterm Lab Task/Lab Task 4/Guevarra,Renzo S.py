#Menu Dictionary
menu = {
    "pizza": 150.00,
    "burger": 120.00,
    "fries": 60.00,
    "americano": 100.00,
    "mocha": 120.00,
    "tiramisu": 130.00,
    "cookies": 90.00,
    "croissant": 90.00,
    "pretzel": 70.00,
    "icecream": 100.00
}

while True:
    #Display the menu
    print("\n-------- MENU --------")
    for item, price in menu.items():
        print(f"{item:<10}: ₱{price:.2f}")
    print("----------------------")

    #Take user orders
    cart = []
    while True:
        order = input("Enter order or (q to quit): ").lower().strip()

        if order == "q":
            break
        elif order in menu:
            cart.append(order)
        else:
            print("Not Available")
            
    #Display Order
    print("\n------ YOUR ORDER ------")
    if cart:
        total = 0
        for item in cart:
            print(f"{item}: ₱{menu[item]:.2f}")
            total += menu[item]
        print("========================")
        print(f"Total: ₱{total:.2f}")
    else:
        print("No items ordered.")
    input("\nPress Enter to continue...")
