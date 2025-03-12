# 4. Write a Python program that calculates the sum of the squares of all odd
# numbers in a list of integers using map() and filter()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def odd_square():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

    # Use map() to square each odd number
    squared_odds = list(map(lambda x: x ** 2, odd_numbers))
    sum_of_squares = sum(squared_odds)

    print("Sum of squares of odd numbers:", sum_of_squares)
    
odd_square()