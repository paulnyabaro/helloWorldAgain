students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]


def get_grade_average(student):
    return student["grade_average"]


valedictorian = max(students, key=get_grade_average)
print(valedictorian)


# Lambda expressions
# Fibonacci series
# lambda a, b: a + b
