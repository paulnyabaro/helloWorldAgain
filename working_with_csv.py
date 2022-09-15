import csv

example_file = open('iris.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))
example_data = list(example_reader)
# print(example_data)
# print(example_data[0][0])


# Writer Objects
# A Writer object lets you write data to a CSV file
output_file = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_file)
print(output_writer.writerow(['spam', 'eggs', 'bacon', 'ham']))
