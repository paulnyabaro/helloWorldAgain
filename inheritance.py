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


class Phone(Item):
    def __int__(self,  name: str, price: float, quantity: int, broken_phones: int):
        # Call to super function to have all the parent attributes
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Prices: ({broken_phones}) should be equal to or greater than zero"

        # Assign to self object
        self.broken_phones = broken_phones


phone4 = Phone("Iphone", 1200, 12)
print(phone4.calculate_total_cost())
# print(phone4.broken_phones)
