# Credit card number validator using Luhn algorithm
credit_card_number = input("Enter the credit card number: ")
while len(credit_card_number) != 16:
    credit_card_number = input("Your credit number is too short or too long.\n"
                               "Please enter the number again: ")
else:
    last_digit = credit_card_number[-1]
    trimmed_cc_number = credit_card_number[:15]
    reversed_cc_number = trimmed_cc_number[::-1]


def double_num(x):
    y = int(x) * 2
    if y > 9:
        y = y - 9
    return y


testing_sum = (double_num(int(reversed_cc_number[0])) + int(reversed_cc_number[1]) +
               double_num(int(reversed_cc_number[2])) + int(reversed_cc_number[3]) +
               double_num(int(reversed_cc_number[4])) + int(reversed_cc_number[5]) +
               double_num(int(reversed_cc_number[6])) + int(reversed_cc_number[7]) +
               double_num(int(reversed_cc_number[8])) + int(reversed_cc_number[9]) +
               double_num(int(reversed_cc_number[10])) + int(reversed_cc_number[11]) +
               double_num(int(reversed_cc_number[12])) + int(reversed_cc_number[13]) +
               double_num(int(reversed_cc_number[14])))

if (float(testing_sum) + float(last_digit)) % 10 == 0:
    print(f"Your credit number is {credit_card_number} and is valid")
else:
    print(f"Your credit number is {credit_card_number} and is invalid")
