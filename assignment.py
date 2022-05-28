import math

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
        

# print(count_couples([1, 2, 1, 2, 3, 2, 2, 4, 5, 1, 3]))

'''
Exercise #4: Write a Program to check Armstrong number
153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153
1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1 + 1296 + 81 + 256 = 1634
'''
def armstrong(armstrong_number):
    sum = 0
    list_number = []
    list_arms = list(str(armstrong_number))   # Split number into list of armstrong number
    for number in list_arms:    
        list_number.append(number)             # Append armstrong number to list
    length = len(list_number)                  # Get length of list to power 
    for i in list_number:
        sum = sum + (math.pow(int(i), length))  # Sum after excute
    if int(sum) == armstrong_number:            # Check
        return True
    return False
# print(armstrong(153))

'''
Exercise #5: Write a Program to find whether a string or number is palindrome or not 
For String-
Enter the number or String
vijay
reverse is:yajiv
The invalid palindrome string

For Number-
Enter the number or String
99
reverse is:99
The valid palindrome string
'''

def palindrome(palindrome_string):
    palindrome_string = str(palindrome_string)  # Set input into string
    negative_string = palindrome_string[::-1]   # Using negative in Python = Reserved value
    if negative_string == palindrome_string:    # Compare input and negative
        print("Valid palindrome string")
    else:
        print("Invalid palindrome string")
# palindrome('lkjjkl')

'''
Exercise #6: Maxtrix Rotation 
Original Maxtrix:
1 2 3
4 5 6
7 8 9
Maxtrix After Rotated 90 degree - clockwise:
7 4 1
8 5 2
9 6 3
Maxtrix After Rotated 90 degree - counterclockwise:
3 6 9
2 5 8
1 4 7
'''
def rotate(matrix, clockwise=True, counterclockwise=True):
    rows = len(matrix)
    cols = len(matrix[0])
    clockwise_list = []
    counterclockwise_list = []
    print("Original Maxtrix:")
    for i in matrix:
        print(i)
    if clockwise:
        print("Maxtrix After Rotated 90 degree - clockwise:")
        for i in range(cols):
            temp = []
            for j in range(rows):
                temp.append(matrix[j][i])
                if len(temp) >= 3:
                    print(temp[::-1])
            clockwise_list.append(temp[::-1])
    if counterclockwise:
        print("Maxtrix After Rotated 90 degree - counterclockwise:")
        for i in range(cols-1, -1, -1):
            temp = []
            for j in range(rows):
                temp.append(matrix[j][i])
                if len(temp) >= 3:
                    print(temp)
            counterclockwise_list.append(temp)

    return clockwise_list, counterclockwise_list


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rotate(matrix)

'''
Exercise #7: Count Letters 
Given string Hello World                                                                                                                                                             
There are 1 letter H in given string                                                                                                                                                 
There are 1 letter e in given string                                                                                                                                                 
There are 3 letter l in given string                                                                                                                                                 
There are 2 letter o in given string                                                                                                                                                 
There are 1 letter W in given string                                                                                                                                                 
There are 1 letter r in given string                                                                                                                                                 
There are 1 letter d in given string	 
'''
def count_letters(letters): 
    set_letter = set(letters.replace(" ", ""))
    for letter in set_letter:
        print("There are {} letter {} in give string".format(letters.count(letter), letter))

# count_letters('Hello World')