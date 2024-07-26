num = int(input())

digit1 = num // 100
digit2 = num % 100 // 10
digit3 = num % 10

max_digit = max(digit1, digit2, digit3)
min_digit = min(digit1, digit2, digit3)

if digit1 != max_digit and digit1 != min_digit:
    mid_digit = digit1
elif digit2 != max_digit and digit2 != min_digit:
    mid_digit = digit2
else:
    mid_digit = digit3

if max_digit + min_digit == mid_digit * 2:
    print("YES")
else:
    print("NO")
