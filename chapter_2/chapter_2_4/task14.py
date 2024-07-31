n = int(input())
m = int(input())
digit_count = len(str(n * m))

num = 1
dn = 1
direction = 1
for i in range(n):
    if direction == 1:
        num = 1 if i == 0 else m * i + 1
        dn = 1
    else:
        num = (i + 1) * m
        dn = -1

    for j in range(m):
        if j == 0:
            print(f"{num}".rjust(digit_count), end="")
        else:
            print(f"{num}".rjust(digit_count + 1), end="")
        num += dn

    direction *= -1
    print("")
