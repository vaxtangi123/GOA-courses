def create_and_sort_list():

    n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    numbers = []
    
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    numbers.sort()
    
    print("Sorted list:", numbers)
    
    return numbers

sorted_list = create_and_sort_list()






numbers = [3, 12, 5, 18, 7, 24, 9, 30, 11, 36, 13]

filtered_numbers = [num for num in numbers if num > 10 and num % 2 == 0]

print(filtered_numbers)



def calculate_area(length, height):
    area = length * height
    return area



rectangle_length = 5
rectangle_height = 10
area_of_rectangle = calculate_area(rectangle_length, rectangle_height)
print("Area of the rectangle:", area_of_rectangle)

