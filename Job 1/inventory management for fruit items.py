import csv

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, fruit_name, unit_price, quantity):
        self.inventory.append({
            'Fruits Name': fruit_name,
            'Unit Price': unit_price,
            'Quantity': quantity,
            'Total price': float(unit_price) * float(quantity)
        })

    def print_summary(self):
        print("Print fruits items summary data from stored CSV file")
        print("['Fruits Name', 'Unit Price', 'Quantity', 'Total price']")
        for item in self.inventory:
            print([item['Fruits Name'], item['Unit Price'], item['Quantity'], item['Total price']])

    def store_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Fruits Name', 'Unit Price', 'Quantity', 'Total price'])
            writer.writeheader()
            writer.writerows(self.inventory)

# Example Usage
if __name__ == "__main__":
    inventory = Inventory()

    num_records = int(input("How many insert Fruits Record? "))
    for i in range(num_records):
        print(f"Enter Fruit record ({i + 1}):")
        fruit_name = input("Enter Fruits Name: ")
        unit_price = input("Enter Unit Price: ")
        quantity = input("Enter quantity: ")
        inventory.add_item(fruit_name, unit_price, quantity)

    inventory.store_to_csv("fruits_inventory.csv")
    inventory.print_summary()