def max_digit(num):
    max = ""
    for digit in num:
        if max == "" or int(digit) > int(max):
            max = digit
    return max


n = int(input())

max_num = ""
for _ in range(n):
    max_num += max_digit(input())

print(max_num)
