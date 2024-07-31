n = int(input())
m = int(input())
digit_count = len(str(n * m))

num = 1
for _ in range(n):
    for j in range(m):
        if j == 0:
            print(f"{num}".rjust(digit_count), end="")
        else:
            print(f"{num}".rjust(digit_count + 1), end="")
        num += 1
    print("")
