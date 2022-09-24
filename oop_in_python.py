class Car:
    # Class attributes
    c_mileage_units = "Mi"
    # Constructor
    def __init__(self, model, year):
        self.i_model = model
        self.i_year = year

    # Special methods
    def __str__(self):
        return f"car with color {self.i_model} and \ mileage {self.i_year}"

    # Class method
    @classmethod
    def print_units(cls):
        print(f'The mileage units: {cls.c_mileage_units}')
        print(f'Class name: {cls.__name__}')

    # Static method
    @staticmethod
    def print_hello():
        print('Hello from a static method')

    # Destructor
    def __del__(self):
        print("Object has been deleted")

car = Car('Toyota', 2010)
# Instant attributes
car.i_color = 'red'
car.i_miles = 10000

print(car.i_model)
print(car.i_color)
Car.print_units()
Car.print_hello()

# Important note
# Attribute names start with c and i to indicate that they are class and instance
# variables, respectively, and not regular local or global variables. The name of
# non-public instance attributes must start with a single or double underscore to
# make them protected or private. This will be discussed later in the chapter.
