import csv

example_file = open('iris.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)