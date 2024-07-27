left = 1
right = 1000

while True:
    mid = (right + left) // 2
    print(mid)

    action = input()
    if action == "Меньше":
        right = mid - 1
    elif action == "Больше":
        left = mid + 1
    elif action == "Угадал!":
        break
