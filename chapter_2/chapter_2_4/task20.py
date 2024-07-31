def convert_to_n_notation(num, n):
    new_num = ""
    while num > 0:
        new_num = str(num % n) + new_num
        num //= n
    return new_num 


def get_digit_sum(num):
    sum = 0
    for digit in num:
        sum += int(digit)
    return sum


if __name__ == "__main__":
    num = int(input())
    
    max_digit_sum = 0
    max_n = 0 
    for n in range(2, 11):
        digit_sum = get_digit_sum(convert_to_n_notation(num, n))
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            max_n = n

    print(max_n)
