class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity in Stock: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0
            print(f"Not enough stock of {self.name}. Quantity is set to 0.")
        else:
            print(f"Updated quantity of {self.name}: {self.quantity}")

    def total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to inventory.")

    def display_inventory(self):
        if len(self.products) == 0:
            print("No products in the inventory.")
        else:
            for product in self.products:
                product.display_info()
                print("-----")

    def calculate_total_inventory_value(self):
        total = sum(product.total_value() for product in self.products)
        print(f"Total value of the inventory: ${total}")


def main():
    inventory = Inventory()

    # Adding products to the inventory
    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Smartphone", 600, 20)
    product3 = Product("Headphones", 150, 30)

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    print("\nDisplaying the inventory:")
    inventory.display_inventory()

    # Updating quantities
    print("\nUpdating quantities:")
    product1.update_quantity(-2)  # Selling 2 Laptops
    product2.update_quantity(5)   # Restocking 5 Smartphones

    print("\nDisplaying the updated inventory:")
    inventory.display_inventory()

    # Calculating the total value of the inventory
    print("\nCalculating total inventory value:")
    inventory.calculate_total_inventory_value()


if __name__ == "__main__":
    main()
