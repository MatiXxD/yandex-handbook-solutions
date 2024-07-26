n = int(input())
m = int(input())

petya_apple_count = 7
vasya_apple_count = 6

petya_apple_count += n - 1 
vasya_apple_count += m + 6

if petya_apple_count > vasya_apple_count:
    print("Петя")
elif vasya_apple_count > petya_apple_count:
    print("Вася")
