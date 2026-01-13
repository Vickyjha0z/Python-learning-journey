#Day 2: Loops and conditions 
#Goal: Count even 

even_odd = 0
odd_count = 0

for number in range(1,11):
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)