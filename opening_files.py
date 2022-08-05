example = open('example.txt')
# example = open('./example.txt') We could also write it in this format, and it will be okay
print(example.read())
example.close()

# Opening a file for reading
# example = open('example.txt', 'r')
# example = open('example.txt', mode='r')

# Opening files for writing
# example = open('example.txt', 'w')
# example = open('example.txt', mode='w')

# Opening files for append mode
# example = open('example.txt', 'a')
# example = open('example.txt', mode='a')
