# even_odd_while.py
# Day 6: Understanding while loop and even/odd logic

#Input: user se number list 
numbers = []
n = int(input(" Enter the number of elements you want to input:"))

count = 0
while count < n:
    num = int(input(f"Number {count+1}:"))
    numbers.append(num)
    count += 1

# Processing: even & odd count
even_count = 0
odd_count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(f"{numbers[i]} is Even")
        even_count += 1
    else:
        print(f"{numbers[i]} is Odd")
        odd_count += 1
    i += 1

# Result summary 
print(f"\nTotal Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")
