class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity


item1 = Item("Phone", 23.77, 21)

print(f"Item: {item1.name}\nPrice: {item1.price}\nQuantity: {item1.quantity}\nTotal cost: {item1.calculate_total_cost()}")