class Beverage:
    def __init__(self, code, name, price, quantity=5):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_available(self):
        return self.quantity > 0

    def vend(self):
        if self.is_available():
            self.quantity -= 1
            return True
        return False


class VendingMachine:
    def __init__(self):
        self.beverages = []
        self.load_beverages()

    def load_beverages(self):
        self.beverages.append(Beverage(1, "Water", 1.00))
        self.beverages.append(Beverage(2, "Soda", 1.50))
        self.beverages.append(Beverage(3, "Juice", 1.75))
        self.beverages.append(Beverage(4, "Iced Tea", 1.25))
        self.beverages.append(Beverage(5, "Coffee", 2.00))
        self.beverages.append(Beverage(6, "Energy Drink", 2.50))

    def display_menu(self):
        print("\n===== VENDING MACHINE MENU =====")
        for drink in self.beverages:
            status = "Available" if drink.is_available() else "OUT OF STOCK"
            print(f"{drink.code}. {drink.name:12} - ${drink.price:.2f} ({status})")
        print("================================")

    def get_drink(self, code):
        for drink in self.beverages:
            if drink.code == code:
                return drink
        return None

    def collect_money(self, price):
        total = 0
        while total < price:
            need = price - total
            print(f"Insert: ${need:.2f} more")
            money = float(input("Add money: "))
            if money > 0:
                total += money
            else:
                print("Please insert a positive amount.")
        return total

    def vend_drink(self, drink):
        print(f"You selected: {drink.name} (${drink.price:.2f})")

        if not drink.is_available():
            print("This item is OUT OF STOCK.")
            return

        total = self.collect_money(drink.price)
        change = total - drink.price

        drink.vend()
        print(f"\nDispensing {drink.name}…")
        if change > 0:
            print(f"Your change: ${change:.2f}")
        print("Thank you! Enjoy your drink.")

    def run(self):
        print("Welcome to the Vending Machine!")

        while True:
            self.display_menu()
            choice = input("Select a drink (1-6): ")

            if not choice.isdigit():
                print("Invalid input. Enter a number 1-6.")
                continue

            code = int(choice)
            drink = self.get_drink(code)

            if drink is None:
                print("Invalid selection.")
                continue

            self.vend_drink(drink)


# Run the vending machine
machine = VendingMachine()
machine.run()
