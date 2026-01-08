# example4_skip_odd_numbers.py
# Task: Sum of only even numbers, skip odd numbers

nums = [1, 2, 3, 4, 5, 6]
total = 0

for num in nums:
    if num % 2 != 0:
        continue  # Skip odd numbers
    total += num

print("Sum of even numbers:", total)