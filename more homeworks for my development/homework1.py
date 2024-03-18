# #homework1

# def check_password():
#     correct_password = "password123"
#     while True:
#         password = input("Enter the password: ")
#         if password == correct_password:
#             print("Correct password! Access granted.")
#             break
#         else:
#             print("Incorrect password. Please try again.")

# check_password()

# #homework2

# def countdown():
#     try:
#         num = int(input("Enter a number to start the countdown: "))
#         if num <= 0:
#             print("Please enter a positive number.")
#         else:
#             print("Countdown starting from", num)
#             while num > 0:
#                 print(num)
#                 num -= 1
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# countdown()

#homework3

def calculate_sum():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            total = sum(range(1, num + 1))
            print("The sum of numbers from 1 to", num, "is:", total)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

calculate_sum()

