def display_menu():
    print("Shopping list Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            # prompt for add an item
        elif choice == "2":
            # prompt for remove an item
        elif choice == "3":
            # display  list
        elif choice == "4":
            # exit
        else:
            print("Invalid choice. Please try again.")
