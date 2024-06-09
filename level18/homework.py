
#homework
def filter_multiples_of_four(numbers_list):
    multiples_of_four = [num for num in numbers_list if num % 4 == 0]
    return multiples_of_four

# Example usage:
numbers = list(range(1, 21))  # Create a list from 1 to 20
filtered_numbers = filter_multiples_of_four(numbers)
print(filtered_numbers)

#homework2

import math

def filter_numbers(initial, final):
    numbers_list = list(range(initial + 1, final))  # Numbers between initial and final
    filtered_list = []
    
    for num in numbers_list:
        if num % 2 == 0:
            filtered_list.append(num ** 2)  # Add square of even numbers
        else:
            filtered_list.append(math.sqrt(num))  # Add square root of odd numbers
    
    return filtered_list

# Ask the user for initial and final numbers
initial_number = int(input("Enter the initial number: "))
final_number = int(input("Enter the final number: "))

result = filter_numbers(initial_number, final_number)
print("Filtered List:", result)


#homework3

def calculate_average(numbers_list):
    if not numbers_list:
        return 0  # Return 0 if the list is empty
    total_sum = sum(numbers_list)
    average = total_sum / len(numbers_list)
    return average

# Example usage:
numbers = [10, 20, 30, 40, 50]
average_result = calculate_average(numbers)
print("Average:", average_result)


#homewor4

def reverse_word(word):
    return word[::-1]

# Example usage:
user_word = input("Enter a word: ")
reversed_word = reverse_word(user_word)
print("Reversed word:", reversed_word)


#homework5

def remove_duplicates(numbers_list):
    return list(set(numbers_list))

# Example usage:
numbers = [1, 2, 3, 2, 4, 3, 5]
filtered_numbers = remove_duplicates(numbers)
print("Filtered List:", filtered_numbers)

