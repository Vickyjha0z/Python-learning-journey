# example3_multiple_pairs.py
# Task: Print all pairs whose sum = target

nums = [1, 2, 3, 4, 5]
target = 5

print("All pairs with sum =", target)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Indexes: {i}, {j} -> Values: {nums[i]}, {nums[j]}")