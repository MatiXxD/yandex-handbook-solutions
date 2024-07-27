def is_simple(num):
    is_simple = True
    n = 2
    while n * n <= num:
        if num % n == 0:
            is_simple = False
        n += 1
    return is_simple


def find_divider(num):
    divider = -1
    for n in range(2, num):
        if num % n == 0 and is_simple(n):
            divider = n
            break
    return divider


if __name__ == "__main__":
    num = int(input())
    is_first = True
    
    divider = find_divider(num)
    while divider != -1:
        if is_first:
            print(divider, end="")
            is_first = False
        else:
            print(f" * {divider}", end="")
        num //= divider
        divider = find_divider(num)
    print(f" * {num}")
