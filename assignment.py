"""
Exercise #1: Fibonacci
Input: n
Output:
n = 7 => 0, 1, 1, 2, 3, 5, 8
n = 11 => 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""
def fibonacci(n):
    """
    Fibonacci numbers are a sequence of numbers where every number is the sum of the preceding two numbers.
    It starts from 0 and 1 as the first two numbers
    """       
    count = 0       # Create count = 0
    first = 0       # Start fron 0 
    second = 1      # and 1
    result = [0, 1] # Append them to result array
    while count <= n - 3:   # Running until count < n - 3 (Why -3? 2 for two numbers, and 1 for index)
        sum_fibo = first + second   # The sum of the previous two numbers
        result.append(sum_fibo)     # Append them to result array
        first = second              # Set the first number into the second number
        second = sum_fibo           # Set the second number into the sum of the preceding two numbers
        count += 1  
    return result
# Call function
# print(fibonacci(11))
"""
Exercise #2: Write a Program to find the second-highest number in an array 
The given array is:
100 14 46 47 94 94 52 86 36 94 89
Second largest number is:94
Largest Number is: 100
"""
def second_highest_number(array):
    list_negative = []
    max_number = max(array)         # Get max number of array
    for i in range (0, len(array)):     
        negative = max_number - array[i]       # Get negative in array of max number
        if negative != 0:   # negative m
            list_negative.append(negative)          
            second_highest = min(list_negative)
            result = max_number - second_highest

    return result   

# print(second_highest_number([100, 14 ,46 ,47 ,94 ,94 ,52 ,86 ,36 ,94 ,89, 98, 91, 99, 99, 100]))

'''
Exercise #3: Count Couples
Input: arr[] = {1, 2, 1, 2, 3, 2, 2, 4, 5, 1, 3}
Output: n = 4
'''
def count_couples(array):
    result = []
    list_div = []
    unique_array = set(array)    # unique array of array list
    for i in unique_array:
        result.append(array.count(i))   # Count appear of elements in array
    for v in result:
        mod = int(v / 2)        # Mod 
        list_div.append(mod)
        couple = sum(list_div)
    return couple
        

print(count_couples([1, 2, 1, 2, 3, 2, 2, 4, 5, 1, 3]))
