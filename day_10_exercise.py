album = {
    "name": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "year of release": 1973,
    "track list": (
            "Speak to Me",
            "Breathe",
            "On the Run",
            "Time",
            "The Great Gig in the Sky",
            "Money",
            "Us and Them",
            "Any Colour You Like",
            "Brain Damage",
            "Eclipse"
        )
}

for key, value in album.items():
    print(f'{key}: {value}')

del album['year of release']

for key, value in album.items():
    print(f'{key}: {value}')

print(album.get('year of release'))