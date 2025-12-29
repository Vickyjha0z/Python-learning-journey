# Day 5: Functions Deep Understanding
# Goal: Find sum from 1 to n using logic

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


n = int(input("Enter a number: "))
result = sum_n(n)

print("Sum from 1 to", n, "is", result)