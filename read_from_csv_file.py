import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)

    @staticmethod
    def check_if_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


Item.instantiate_from_csv()

print(Item.check_if_integer(7))
print(Item.check_if_integer(4.0))
print(Item.check_if_integer(7.2))