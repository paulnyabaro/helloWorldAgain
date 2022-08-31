import pandas as pd

movies = {
    "title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
    "director": ("Christopher Nolan", "Gore Verbinski"),
    "year": (2010, 2003)
}


df = pd.DataFrame(movies).rename(columns={"year": "release_year"})

print(df)
print(df.head())