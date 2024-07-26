petya_score = int(input())
vasya_score = int(input())
tolya_score = int(input())

max_score = max(petya_score, vasya_score, tolya_score)

if max_score == petya_score:
    print("Петя")
elif max_score == vasya_score:
    print("Вася")
else:
    print("Толя")
