def is_simple(num):
    if num == 1:
        return False

    simple = True
    n = 2
    while n * n <= num:
        if num % n == 0:
            simple = False
        n += 1
    return simple


n = int(input())

simple_count = 0
for i in range(1, n + 1):
    if is_simple(int(input())):
        simple_count += 1

print(simple_count)
