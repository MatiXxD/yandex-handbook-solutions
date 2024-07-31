n = int(input())
m = int(input())
digit_count = len(str(n * m))

for num in range(1, n + 1):
    for j in range(m):
        if j == 0:
            print(f"{num + j * n}".rjust(digit_count), end="")
        else:
            print(f"{num + j * n}".rjust(digit_count + 1), end="")
    print("")
