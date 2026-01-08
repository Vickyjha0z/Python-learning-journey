# example5_largest_pair_sum.py
# Task: Find the largest sum of any two numbers

nums = [3, 7, 2, 9, 5]
max_sum = float('-inf')
pair = ()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] > max_sum:
            max_sum = nums[i] + nums[j]
            pair = (nums[i], nums[j])

print(f"Largest pair sum: {max_sum} -> Values: {pair}")