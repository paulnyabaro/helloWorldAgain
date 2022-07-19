class Item:
    pay_rate = 0.8

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

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # def __repr__(self):
    #     return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 1250, 4)
item2 = Item("Macbook", 1800, 2)
item2.pay_rate = 0.7

print(f"Item 1: {item1.name}\nPrice: ${item1.price}\nQuantity: {item1.quantity}"
      f"\nTotal cost: ${item1.calculate_total_cost()}\n" + "*" * 20)

print(f"Item 2: {item2.name}\nPrice: ${item2.price}\nQuantity: {item2.quantity}"
      f"\nTotal cost: ${item2.calculate_total_cost()}\n" + "*" * 20)

print(f"Total Items: {item1.quantity + item2.quantity},"
      f" Total price: ${item1.calculate_total_cost() + item2.calculate_total_cost()}")

print(f"Total cost after discount: "
      f"${item1.calculate_total_cost() * item1.pay_rate + item2.calculate_total_cost() * item2.pay_rate}")
