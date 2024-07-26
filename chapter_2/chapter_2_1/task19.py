name = input()
price = int(input())
weight = int(input())
paid = int(input())

total_price = weight * price

align_number = 35
print("Чек".center(align_number, "="))
print("Товар: " + f"{name}".rjust(align_number - 7))
print("Цена: " + f"{weight}кг * {price}руб/кг".rjust(align_number - 6))
print("Итого: " + f"{total_price}руб".rjust(align_number - 7))
print("Внесено: " + f"{paid}руб".rjust(align_number - 9))
print("Сдача: " + f"{paid-total_price}руб".rjust(align_number - 7))
print("=" * align_number)
