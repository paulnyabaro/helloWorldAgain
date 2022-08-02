card_number = input('Please enter your Credit Card Number: ')
while len(card_number) != 16:
    card_number = input('The number is too short or too long\nPlease try again! ')
else:
    credit_card_number = list(card_number)
    check_sum = credit_card_number.pop()
    credit_card_number.reverse()
processed_digits = []
for index, digit in enumerate(credit_card_number):
    if index % 2 == 0:
        new_digit = int(digit) * 2

        if new_digit > 9:
            new_digit -= 9

        processed_digits.append(new_digit)
    else:
        processed_digits.append(int(digit))

total_digits_sum = int(check_sum) + sum(processed_digits)
if total_digits_sum % 10 == 0:
    print(f'Your Credit Card Number {card_number} is valid')

else:
    print(f'Your Credit Card Number {card_number} is invalid')