n = int(input())
m = int(input())
digit_count = len(str(n * m))

for num in range(1, n + 1):
    for j in range(m):
        if j == 0:
            print(f"{num}".rjust(digit_count), end="")
        elif j % 2 != 0:
            print(f"{(j + 1) * n - num + 1}".rjust(digit_count + 1), end="")
        else:
            print(f"{j * n + num}".rjust(digit_count + 1), end="")
    print("")
