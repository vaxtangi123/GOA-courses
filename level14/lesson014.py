#homework1

numbers_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(numbers_array)

#homework2


# Original array
original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# New array with even numbers
even_array = [num for num in original_array if num % 2 == 0]

# Print the new array
print("Original Array:", original_array)
print("New Array with Even Numbers:", even_array)

#homework3


# Create an array and add numbers from 50 to 100
my_array = []

for num in range(50, 101):
    my_array.append(num)

# Print the array
print("Array:", my_array)

# Print the last three elements using negative indexing
print("Last three elements using negative indexing:", my_array[-3:])


#HOMEWORK4

# Get two integer inputs from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Determine the lower and higher numbers
lower_num = min(num1, num2)
higher_num = max(num1, num2)

# Use a for loop to iterate from the lower number to the higher number
print(f"Multiples of five between {lower_num} and {higher_num}:")

for i in range(lower_num, higher_num + 1):
    # Use if statement to print multiples of five
    if i % 5 == 0:
        print(i)


#HOMEWORK5


# Create an empty array
names_array = []

# Ask user for age
age = int(input("What is your age? "))

# Check if the user is over 18
if age > 18:
    # Ask for the user's name
    name = input("What is your name? ")
    
    # Add the name to the array
    names_array.append(name)

    # Print the updated array
    print("Names array:", names_array)
else:
    print("You are not eligible to provide your name.")

        
        

        