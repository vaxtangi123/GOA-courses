#homework1

numbers_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers_array)


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


#homework2

numbers_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers_array = [num for num in numbers_array if num % 2 == 0]
print(even_numbers_array)


[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#homework3

# Create an empty array
my_array = []

# Add numbers from 50 to 100 to the array
for num in range(50, 101):
    my_array.append(num)

# Print the part of the array with negative indexes
print(my_array[-1:-11:-1])

[100, 99, 98, 97, 96, 95, 94, 93, 92, 91]

 #homework4

# Ask the user for two inputs and store them as integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Determine the lower and higher numbers
start_num = min(num1, num2)
end_num = max(num1, num2)

# Use a for loop to iterate from the lower number to the higher number
for num in range(start_num, end_num + 1):
    # Check if the number is a multiple of five
    if num % 5 == 0:
        print(num)

#homework5
        
# Create an empty array
names_array = []

# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the age is over 18
if age > 18:
    # Ask the user for their name
    name = input("Please enter your name: ")
    # Add the name to the array
    names_array.append(name)

# Print the array
print(names_array)
