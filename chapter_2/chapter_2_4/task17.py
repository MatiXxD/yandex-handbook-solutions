n = int(input())

count = 0
for _ in range(n):
    txt = input()
    if txt == txt[::-1]:
        count += 1
print(count)
