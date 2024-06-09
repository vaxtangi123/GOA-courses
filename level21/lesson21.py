def multiply(values):
    result = 1
    for num in values:
        result *= num
    return result

print(multiply([1, 2, 3, 4]))

#2-davaleba

def bmi(weight, height):
    height_squared = height * height
    bmi_value = weight / height_squared
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"


#3-davaleba


def vowel_count(text):
    count = 0
    for i in text:
        if i in "aeiou":
            count+=1
    return f"{text} in your name is {count} vowels"


#4-davaleba

if square_digits(num):
    res_str = ""
    num_str = str(num)
    for i in num_str:
        res_str += str(int(i)**2)
    return int(res_str)


print(square_digits(9199))


#5-davaleba




def descending_order(num):
    num = str(num)
    num = list(num)
    num = sorted(num)
    num = reversed(num)
    num = "".join(num)
    return int(num)

print(descending_order(42145))

#6-davaleba


def likes(names):
    num_likes = len(names)
    
    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_likes - 2} others like this"


#7-davaleba

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum+=i
    return sum
