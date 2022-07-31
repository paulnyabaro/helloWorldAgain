movie = ('The fast and the furious', 'Jim Someone', 2000000)

movie_name, director, budget = movie

print(f"For the movie {movie_name}, the director was, {director} and the budget was {budget}")


movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for title, director, year in movies:
    print(f"{title} ({year}), by {director}")

# Using enumerate function
names = ["Harry", "Rachel", "Brian"]

for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")

# The braces are very important
for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")
