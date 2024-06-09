def num(number):
    result = 0
    for i in number:
        result +=i
    return result


number = [1,2,3,]
print(num(number))


def num(numbe):
    result = 0
    for i in numbe:
            result = i
    return result


number = [1,2,3,4]
print(num(number))


def num(number):
    return min(number) 

number1 = [5, 3, 8, 2, 7]
print(num(number1))


def num(number):
    count = 0
    for _ in number:
        count += 1
    return count
number5 = [10, 20, 30,]
print(num(number5))


def num(number):
    result = []
    for i in number:
        result.append(i)
    return result
number5 = [10, 20, 30,]
number6 = num(number5)
print(number5)
print(number6)