from typing import Union, Any, List, Tuple

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

# Working with tuples
movie: Tuple[str, str, int] = ("Toy Story 3", "Lee Unkrich", 2010)
print(names_two)

# Annotating functions
Movie = Tuple[str, str, int]

def show_movies(movies: List[Movie]):
    for title, director, year in movies:
        print(f"{title} ({year}), by {director}")

movies: List[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)