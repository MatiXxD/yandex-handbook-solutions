a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b != 0:
        if c == 0:
            print(f"{c:.2f}")
        else:
            print(f"{-c/b:.2f}")
    elif c != 0:
        print("No solution")
    else:
        print("Infinite solutions")
else:
    d = b**2 - 4 * a * c
    if d < 0:
        print("No solution")
    elif d == 0:
        print(f"{-b/(2*a):.2f}")
    else:
        root1 = (-b + d ** (1 / 2)) / (2 * a)
        root2 = (-b - d ** (1 / 2)) / (2 * a)
        print(f"{min(root1, root2):.2f} {max(root1, root2):.2f}")
