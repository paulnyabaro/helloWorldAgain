from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)
print(a_words)
