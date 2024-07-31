n = int(input())

total_sum = 0
for _ in range(n):
    num = input()
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    total_sum += digit_sum

print(total_sum)
