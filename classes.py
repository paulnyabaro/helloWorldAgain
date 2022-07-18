class Item:
    def __init__(self, name: str, price: float, quantity: int):

        # Run validations to the received arguments
        assert price >= 0, f"Prices: ({price}) should be greater than zero"
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity


item1 = Item("Phone", 1250, 4)
item2 = Item("Macbook", 1800, 2)

print(f"Item 1: {item1.name}\nPrice: ${item1.price}\nQuantity: {item1.quantity}"
      f"\nTotal cost: ${item1.calculate_total_cost()}\n" + "*" * 20)

print(f"Item 2: {item2.name}\nPrice: ${item2.price}\nQuantity: {item2.quantity}"
      f"\nTotal cost: ${item2.calculate_total_cost()}\n" + "*" * 20)

print(f"Total Items: {item1.quantity + item2.quantity},"
      f" Total price: ${item1.calculate_total_cost() + item2.calculate_total_cost()}")


