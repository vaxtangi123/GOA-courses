#homework1

def calculate_sum(numbers_list):
    # Initialize a variable to store the sum
    total_sum = 0
    
    # Iterate through the numbers in the list and add them to the sum
    for num in numbers_list:
        total_sum += num
    
    # Return the total sum
    return total_sum

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print("Sum of numbers:", result)

             #homework2

def filter_long_strings(strings_list):
    # Initialize an empty list to store the filtered strings
    filtered_list = []
    
    # Iterate through the strings in the input list
    for string in strings_list:
        # Check if the length of the string is greater than 5
        if len(string) > 5:
            # Add the string to the filtered list
            filtered_list.append(string)
    
    # Return the filtered list
    return filtered_list

# Example usage:
words = ["apple", "banana", "orange", "watermelon", "grape"]
filtered_words = filter_long_strings(words)
print("Filtered words:", filtered_words)

              #homework3

def filter_even_numbers(numbers_list):
    # Initialize an empty list to store the even numbers
    even_numbers_list = []
    
    # Iterate through the numbers in the input list
    for num in numbers_list:
        # Check if the number is even
        if num % 2 == 0:
            # Add the even number to the list
            even_numbers_list.append(num)
    
    # Return the list of even numbers
    return even_numbers_list

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)

              #homework4
def find_largest_number(numbers_list):
    # Check if the list is empty
    if not numbers_list:
        return None
    
    # Initialize the largest number as the first element of the list
    largest_number = numbers_list[0]
    
    # Iterate through the numbers in the list starting from the second element
    for num in numbers_list[1:]:
        # Update the largest number if a larger number is found
        if num > largest_number:
            largest_number = num
    
    # Return the largest number
    return largest_number

# Example usage:
numbers = [3, 7, 2, 10, 5, 8]
largest_num = find_largest_number(numbers)
print("Largest number:", largest_num)


                #homework5

def filter_strings_starting_with_a(strings_list):
    # Initialize an empty list to store the strings starting with 'a'
    filtered_list = []
    
    # Iterate through the strings in the input list
    for string in strings_list:
        # Check if the string starts with 'a'
        if string.lower().startswith('a'):
            # Add the string to the filtered list
            filtered_list.append(string)
    
    # Return the filtered list
    return filtered_list

# Example usage:
words = ["apple", "banana", "orange", "apricot", "grape"]
filtered_words = filter_strings_starting_with_a(words)
print("Filtered words starting with 'a':", filtered_words)


                 #homework6

def calculate_square(numbers_list):
    # Initialize an empty list to store the squares
    squared_list = []
    
    # Iterate through the numbers in the input list
    for num in numbers_list:
        # Calculate the square of the number and add it to the squared list
        squared_list.append(num ** 2)
    
    # Return the squared list
    return squared_list

# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = calculate_square(numbers)
print("Squared numbers:", squared_numbers)


                  #homework7

def calculate_string_lengths(strings_list):
    # Initialize an empty list to store the lengths
    lengths_list = []
    
    # Iterate through the strings in the input list
    for string in strings_list:
        # Calculate the length of the string and add it to the lengths list
        lengths_list.append(len(string))
    
    # Return the lengths list
    return lengths_list

# Example usage:
words = ["apple", "banana", "orange", "watermelon", "grape"]
lengths = calculate_string_lengths(words)
print("Lengths of strings:", lengths)

                  #homework8
def sum_numbers_greater_than_10(numbers_list):
    # Use a list comprehension to filter numbers greater than 10 and calculate their sum
    total_sum = sum(num for num in numbers_list if num > 10)
    
    # Return the total sum
    return total_sum

# Example usage:
numbers = [5, 10, 15, 20, 25]
sum_greater_than_10 = sum_numbers_greater_than_10(numbers)
print("Sum of numbers greater than 10:", sum_greater_than_10)


