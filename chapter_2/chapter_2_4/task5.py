n = int(input())

count = 0
for _ in range(n):
    flag = False
    txt = input()
    while txt != "ВСЁ":
        if txt == "зайка" and not flag:
            flag = True
        txt = input()
    if flag:
        count += 1

print(count)
