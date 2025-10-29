items = []

def menu():
    while True:
        print("\nWelcome to 7OOP ProgramCart")
        print("1 - Add Items")
        print("2 - Search for an Item")
        print("3 - Remove an Item")
        print("4 - View all items")
        print("0 - Exit program")

        choice = input("Enter choice [0 to quit]: ")

        if choice == "1":
            while True:
                newItem = input("Enter item to add (or 'x' to stop): ").upper()
                if newItem == "X":
                    break
                items.append(newItem)
            print("Items added successfully.")

        elif choice == "2":
            search = input("Enter item to search: ").upper()
            count = items.count(search)
            if count > 0:
                print("-------------------------------")
                print(f"Item '{search}' found {count} time(s) in the list.")
                print("-------------------------------")
            else:
                print(f"Item '{search}' not found.")

        elif choice == "3":
            remove = input("Enter item to remove: ").upper()
            if remove in items:
                items.remove(remove)
                print(f"Item '{remove}' found and deleted.")
            else:
                print(f"Item '{remove}' not found - deletion unsuccessful.")

        elif choice == "4":
            if len(items) == 0:
                print("The list is empty.")
            else:
                print("\n--- Items in the List ---")
                for i, item in enumerate(items, 1):
                    print(f"{i}. {item}")

        elif choice == "0":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

menu()
