n = int(input())

print("А Б В")
for a in range(1, n - 1):
    for b in range(1, n - a):
        for v in range(n - a - b, 0, -1):
            if a + b + v == n:
                print(f"{a} {b} {v}")
