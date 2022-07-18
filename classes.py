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


item1 = Item("Phone", 23.77, 12)

print(f"Item: {item1.name}\nPrice: ${item1.price}\nQuantity: {item1.quantity}\nTotal cost: ${item1.calculate_total_cost()}")