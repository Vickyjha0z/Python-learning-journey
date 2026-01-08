# example2_two_sum_negative.py
# Task: Handle negative numbers too

nums = [-1, 2, 7, -3]
target = 4

print("Pairs with sum =", target)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Indexes: {i}, {j} -> Values: {nums[i]}, {nums[j]}")