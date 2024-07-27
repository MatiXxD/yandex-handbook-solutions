n = int(input())

count = 0
for _ in range(n):
    txt = input()
    if "зайка" in txt:
        count += 1
print(count)
