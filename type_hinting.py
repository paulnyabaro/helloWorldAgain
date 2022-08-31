from typing import Union
from typing import Any
from typing import List

name: str = "Paul"
age: int = 25
height_cm: Union[int, float] = 170
Progress: Any = "25%"
loves_python: bool = True

print(height_cm)

# Annotating collections
names: List = ["Liz", "Rick", "Jerry"]
names_two: List[str] = ["Summer", "Morty", "Beth"]

# We can also use Union on lists ->
names_three: List[Union[str, int]] = ["x", 13, "camel", 0]

print(names_two)