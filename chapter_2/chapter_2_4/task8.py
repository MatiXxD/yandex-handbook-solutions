def get_digit_sum(num):
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    return digit_sum


n = int(input())

winner_name = input()
winner_score = get_digit_sum(input())
for _ in range(n - 1):
    name = input()
    score = get_digit_sum(input())
    if score >= winner_score:
        winner_score = score
        winner_name = name

print(winner_name)
