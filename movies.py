movies_list = [
    ("Avengers: Endgame", " Anthony Russo", 2019, "356 million",)
]

new_movie_name = input("Enter the name of the new movie ")
new_movie_director = input(f"Who directed {new_movie_name.title()}? ")
new_movie_release_year = input(f"When was {new_movie_name.title()} released? ")
new_movie_budget = input(f"What was {new_movie_name.title()}'s budget? ")

new_movie_info = (new_movie_name, new_movie_director, new_movie_release_year, new_movie_budget)

movies_list.append(new_movie_info)

print(f"New movie details \n **********\nName: {new_movie_name} \nRelease year: {new_movie_release_year}\n **********")
print(movies_list)
movies_list.pop(0)
print(movies_list)
