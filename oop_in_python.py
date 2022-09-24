class Car:
    def __init__(self, c_model, year):
        self.c_model = c_model
        self.year = year


car = Car('Toyota', 2010)
# Instant attributes
car.color = 'red'
car.miles = 10000

print(car.c_model)
print(car.color)