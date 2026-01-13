arr = [3, 7, 5, 2]

max_num = float('-inf')
second_max = float('-inf')

for i in arr:
    if i > max_num:
        second_max = max_num
        max_num = i
    elif i > second_max and i != max_num:
        second_max = i

print("Second Largest =", second_max)