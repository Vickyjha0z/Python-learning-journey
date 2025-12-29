# Day 4: User Input with List
# Goal: Take multiple inputs safely and process them

def count_even_odd(numbers):
    even = 0
    odd = 0

    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd   

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

e, o = count_even_odd(numbers)  

print("Even numbers: " , e)
print("Odd numbers: " , o)







    