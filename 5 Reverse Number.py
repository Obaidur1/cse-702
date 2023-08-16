def reverse_number(number):
    rev_number = 0
    while number > 0:
        last_digit = number % 10
        rev_number = rev_number * 10 + last_digit
        number //= 10
    return f"Reversed number is: {rev_number}"


num = reverse_number(345)
print(num)
