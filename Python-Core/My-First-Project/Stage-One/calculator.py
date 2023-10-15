def main():
    menu = initialize_menu()
    list_menu(menu)


def list_menu(menu):
    print("Prices:")
    for item in menu:
        print(menu[item])


def initialize_menu():

    menu = {"Bubblegum": Item("Bubblegum", 2),
            "Toffee": Item("Toffee", 0.2),
            "Ice_cream": Item("Ice cream", 5),
            "Milk_chocolate": Item("Milk chocolate", 4),
            "Doughnut": Item("Doughnut", 2.5),
            "Pancake": Item("Pancake", 3.2)
            }
    return menu


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: (${self.price})"


if __name__ == "__main__":
    main()