# Taco Palace Ordering System

# Function to print the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $3.75")
    print("3. Nachos - $4.25")
    print("4. Soft Drink - $1.95")
    print("5. Quit")

# Function to get price of food item
def get_price(choice):
    prices = {
        1: 2.50,  # Taco
        2: 3.75,  # Burrito
        3: 4.25,  # Nachos
        4: 1.95   # Soft Drink
    }
    return prices.get(choice, 0)

# Function to get name of food item
def get_item_name(choice):
    items = {
        1: "Taco",
        2: "Burrito",
        3: "Nachos",
        4: "Drink"
    }
    return items.get(choice, "Unknown")

def main():
    print("Welcome to Taco Palace! Please view the menu below and make a selection")

    order = []       # list to store ordered items
    total = 0.0      # running total price

    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 5:  # Quit option
            break
        elif 1 <= choice <= 4:
            item = get_item_name(choice)
            price = get_price(choice)
            order.append(item)
            total += price
            print(f"You selected a {item}")
        else:
            print("Invalid choice. Please select between 1 and 5.")

    # Final order summary
    if order:
        print("\nYou ordered:", ", ".join(order))
        print(f"Your total is ${total:.2f}")
    else:
        print("\nYou did not order anything.")

# Run the program
if __name__ == "__main__":
    main()
