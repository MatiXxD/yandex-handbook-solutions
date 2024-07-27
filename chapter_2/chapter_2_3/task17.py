num = int(input())

new_num = 0
mlt = 1
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        new_num += mlt * digit
        mlt *= 10 
    num //= 10

print(new_num)
