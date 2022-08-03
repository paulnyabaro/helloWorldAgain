def get_even_numbers(number=6):
    for num in range(number):
        print((num + 1) * 2)


get_even_numbers(8)


def draw_patters(symbol, num_range):
    for _ in range(num_range):
        print(symbol * _)


draw_patters("*", 8)
draw_patters("-", 18)
draw_patters("^", 16)
