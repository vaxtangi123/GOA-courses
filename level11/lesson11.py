#homework1

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#homework2

for num in range(1, 21):
    if num % 2 == 0:
        print(num)

#homework3

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    sum += num
    num -= 1

print("The sum is:", sum)

#homework4


pin = input("Enter your PIN: ")

if pin == "1234":
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Balance")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Withdrawal selected")
    elif choice == 2:
        print("Deposit selected")
    elif choice == 3:
        print("Balance selected")
    else:
        print("Invalid choice")
else:
    print("Incorrect PIN")


#homework5

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Login successful")
else:
    print("Invalid username or password")
