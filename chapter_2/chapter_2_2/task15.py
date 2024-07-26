num1 = int(input())
num2 = int(input())

digit11 = num1 // 10
digit12 = num1 % 10
digit21 = num2 // 10
digit22 = num2 % 10

max_digit = max(digit11, digit12, digit21, digit22)
min_digit = min(digit11, digit12, digit21, digit22)

mid_sum = digit11 + digit12 + digit21 + digit22 - max_digit - min_digit
if mid_sum >= 10:
    mid_sum %= 10

print(f"{max_digit}{mid_sum}{min_digit}")
