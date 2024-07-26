password = int(input())

new_password_part_1 = (password % 100 // 10) + (password % 10)
new_password_part_2 = (password % 100 // 10) + (password // 100)

new_password = f"{max(new_password_part_1, new_password_part_2)}{min(new_password_part_1, new_password_part_2)}"
print(new_password)
