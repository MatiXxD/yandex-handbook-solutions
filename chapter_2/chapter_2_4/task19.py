size = int(input())
half_size = size // 2 + 1 if size % 2 else size // 2
is_even = 1 if size % 2 == 0 else 0

width = len(str(half_size))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        row_val = i if (i <= half_size) else half_size - ((i - is_even) % half_size)
        col_val = j if j <= half_size else half_size - ((j - is_even) % half_size)

        num = min(row_val, col_val)
        end_with = "" if j == size else " "
        print(str(num).rjust(width), end=end_with)
    print("")
