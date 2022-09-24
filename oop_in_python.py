class Car:
    # Class attributes
    c_mileage_units = "Mi"
    # Constructor
    def __init__(self, model, year):
        self.i_model = model
        self.i_year = year

    # Destructor
    def __del__(self):
        print("Object has been deleted")

car = Car('Toyota', 2010)
# Instant attributes
car.i_color = 'red'
car.i_miles = 10000

print(car.i_model)
print(car.i_color)
#
# Important note
# Attribute names start with c and i to indicate that they are class and instance
# variables, respectively, and not regular local or global variables. The name of
# non-public instance attributes must start with a single or double underscore to
# make them protected or private. This will be discussed later in the chapter.
