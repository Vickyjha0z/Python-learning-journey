# example1_two_sum_simple.py
# Task: Find indexes of two numbers whose sum = target

nums = [1, 4, 5, 7]
target = 9

print("Pairs with sum =", target)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Indexes: {i}, {j} -> Values: {nums[i]}, {nums[j]}")