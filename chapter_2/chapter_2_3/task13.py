names_count = int(input())

if names_count != 0:
    max_name = input()
    for _ in range(names_count - 1):
        name = input()
        if name < max_name:
            max_name = name
    print(max_name)
