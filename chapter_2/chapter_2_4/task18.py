def get_width(s, e):
    line = ""
    for i in range(s, e):
        if i != s:
            line += f" {i}"
        else:
            line += str(i)
    return len(line)


if __name__ == "__main__":
    n = int(input())
    last_num = n

    prv_row_num = 0
    last_row_num = 1
    prv_row_len = 0
    last_row_len = 1
    n -= 1

    row_count = 1
    while n > 0:
        prv_row_num = last_row_num
        prv_row_len = last_row_len
        last_row_num += prv_row_len
        last_row_len = prv_row_len + 1
        if last_row_len > n:
            last_row_len = n

        n -= last_row_len
        row_count += 1

    prv_width = get_width(prv_row_num, prv_row_num + prv_row_len)
    last_width = get_width(last_row_num, last_row_num + last_row_len)
    width = max(prv_width, last_width)

    num = 1
    for i in range(row_count):
        line = ""
        for j in range(i + 1):
            if num > last_num:
                continue
            if j == 0:
                line += str(num)
            else:
                line += f" {num}"
            num += 1
        if (width + len(line)) % 2 == 0:
            print(line.center(width))
        else:
            print(line.center(width - 1))
