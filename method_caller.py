from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)
print(a_words)

# for word in a_words:
#     print(word)
#

# Using next functions
first_word = next(a_words)
print(first_word)
