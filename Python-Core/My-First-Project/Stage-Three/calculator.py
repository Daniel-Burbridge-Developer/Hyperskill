def main():
    menu = initialize_default_menu()
    # print(menu)
    override_profits_on_items(menu)
    print(menu.print_profits_by_item())
    stage_four(menu)

def stage_four(menu):
    income = menu.profits
    staff_expenses = int(input("Staff expenses: "))
    other_expenses = int(input("Other expenses: "))

    net_income = (income - staff_expenses - other_expenses)
    print(f"Net income: ${net_income}")

def override_profits_on_items(menu):
    menu.items["Bubblegum"].set_profits(202)
    menu.items["Toffee"].set_profits(118)
    menu.items["Ice_cream"].set_profits(2250)
    menu.items["Milk_chocolate"].set_profits(1680)
    menu.items["Doughnut"].set_profits(1075)
    menu.items["Pancakes"].set_profits(80)


def initialize_default_menu():
    return Menu("Default Menu", {
            "Bubblegum": Item("Bubblegum", 2),
            "Toffee": Item("Toffee", 0.2),
            "Ice_cream": Item("Ice cream", 5),
            "Milk_chocolate": Item("Milk chocolate", 4),
            "Doughnut": Item("Doughnut", 2.5),
            "Pancakes": Item("Pancake", 3.2)
            })


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.sales = 0
        self.profits = 0

    def __str__(self):
        return f"{self.name}: ${self.price}"

    def increment_sales_and_profits(self):
        self.sales += 1
        self.profits += self.price

    def set_sales(self, amount_sold):
        self.sales = amount_sold
        self.profits = self.price * amount_sold

    def set_profits(self, profit):
        self.profits = profit

class Menu:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.profits = 0

    def __str__(self):
        s = ""
        s += "Prices:"
        s += "\n"
        for item in self.items:
            s += str(self.items[item])
            s += "\n"

        return s

    def print_profits_by_item(self):
        s = ""
        s += "Earned Amount:"
        s += "\n"
        for item in self.items:
            s += f'{self.items[item]}: ${self.items[item].profits}'
            s += "\n"

        self.calc_total_profit()
        s += '\n'
        s += f'Income: ${self.profits}'

        return s

    def override_profit_on_item(self, item, profit):
        self.items[item].set_profits(profit)

    def calc_total_profit(self):
        self.profits = 0
        for item in self.items:
            self.profits += self.items[item].profits


if __name__ == "__main__":
    main()
