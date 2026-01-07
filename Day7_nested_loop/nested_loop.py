# Day 7: Nested Loops & Pattern Printing in Python 
# Goal: Print a pyramid-like number pattern using nested loops

rows = 5  # Numbers of rows in the pattern

for i in range(1 , rows +1):
    # Print leading spaces for Pyramid alignment
    for j in range( rows -1):
        print(" ", end=" ")

    # Print numbers from 1 to i in each row
    for j in range(1, i+1):
        print(j, end=" ")

    # Move to next line after each row
    print()         

        