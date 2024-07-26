petya_score = int(input())
vasya_score = int(input())
tolya_score = int(input())

max_score = max(petya_score, vasya_score, tolya_score)
min_score = min(petya_score, vasya_score, tolya_score)

width = 8
if petya_score == max_score:
    print("Петя".center(width * 3))
elif vasya_score == max_score:
    print("Вася".center(width * 3))
else:
    print("Толя".center(width * 3))

if petya_score != max_score and petya_score != min_score:
    print("Петя".center(width))
elif vasya_score != max_score and vasya_score != min_score:
    print("Вася".center(width))
else:
    print("Толя".center(width))

if petya_score == min_score:
    print(" " * 2 * width + "Петя".center(width))
elif vasya_score == min_score:
    print(" " * 2 * width + "Вася".center(width))
else:
    print(" " * 2 * width + "Толя".center(width))

print("II".center(width) + "I".center(width) + "III".center(width)) 
