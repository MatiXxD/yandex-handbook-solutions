nums_count = int(input())

num = 1
left_nums = nums_count
nums_in_row = 1
while num <= nums_count:
    for _ in range(nums_in_row):
        print(num, end=" ")
        num += 1
        left_nums -= 1
    nums_in_row += 1
    if nums_in_row > left_nums:
        nums_in_row = left_nums
    print("")
