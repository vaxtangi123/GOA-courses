def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    
    return sorted_numbers[0] + sorted_numbers[1]



def filter_friends(names):
    friends = []
    for name in names:
        if len(name) == 4:
            friends.append(name)

    return friends
names = ["Ryan", "Kieran", "Mark"]
print(filter_friends(names))