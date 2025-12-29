# Day 3: Functions
# Goal: Seperate logic using functions

def count_even_odd(numbers):
    even = 0
    odd = 0

    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd     

nums =[10, 13, 15 ,16 ,18]  
even_count, odd_count = count_even_odd(nums)    

print("Even:", even_count)
print("Odd:", odd_count)
        