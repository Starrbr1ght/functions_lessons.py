# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(list_of_numbers):
    for number in list_of_numbers:
        if number <= 0:
            return False
    return True

numbers = [1, -5, 3, 0, 10, -2, 7]






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
def sum_less(numbers_list):
    """
    Adds the numbers of a list as long as they are greater than 0 and less than 1000,
    and returns the result of said sum.
    """
    total_sum = 0
    for num in numbers_list:
        if 0 < num < 1000:
            total_sum += num
    return total_sum

numbers = [10, -5, 500, 1001, 25, 999, 0]
result = sum_less(numbers)
print(f"The numbers list to test is: {numbers}")
print(f"The sum of numbers greater than 0 and less than 1000 is: {result}")



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even (numbers):
    count=0
    for num in numbers:
        if num % 2 == 0:
            count +=1
            return count