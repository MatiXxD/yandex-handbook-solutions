num = int(input())

digit1 = num // 100
digit2 = num % 100 // 10
digit3 = num % 10

max_digit = max(digit1, digit2, digit3)
min_digit = min(digit1, digit2, digit3)
mid_digit = digit1 + digit2 + digit3 - max_digit - min_digit

if min_digit != 0:
    min_number = min_digit * 10 + mid_digit
elif mid_digit != 0:
    min_number = mid_digit * 10 + min_digit
else:
    min_number = max_digit * 10 + min_digit

max_number = max_digit * 10 + mid_digit
print(min_number, max_number)
