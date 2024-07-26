petya_score = int(input())
vasya_score = int(input())
tolya_score = int(input())

max_score = max(petya_score, vasya_score, tolya_score)
min_score = min(petya_score, vasya_score, tolya_score)

if petya_score == max_score:
    print("1. Петя")
elif vasya_score == max_score:
    print("1. Вася")
else:
    print("1. Толя")

if petya_score != max_score and petya_score != min_score:
    print("2. Петя")
elif vasya_score != max_score and vasya_score != min_score:
    print("2. Вася")
else:
    print("2. Толя")

if petya_score == min_score:
    print("3. Петя")
elif vasya_score == min_score:
    print("3. Вася")
else:
    print("3. Толя")
