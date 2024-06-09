
# codewars 8-kyu


# 1-Count the Monkeys!

# def monkey_count(n):
#     result = []
#     for i in range(1,n + 1):
#         result.append(i)
#     return result


# 2 -Remove First and Last Character

# def remove_char(s):
#     return s[1:-1]


# 3 - Remove exclamation marks

# def remove_exclamation_marks(s):
#         return s.replace("!", "")


# 4 - Sum of positive

# def positive_sum(arr):
#     result = 0
#     for i in arr:
#         if i > 0:
#             result+=i
#     return result

# 5 - Remove String Spaces

# def no_space(x):
#     result = ""

#     for i in x:
#         if i != " ":
#             result = result + i
#     return result

#2-davaleba




# codewars 7-kyu


# 1 -Square Every Digit


# def square_digits(num):
#     res_str = ""
#     num_str = str(num)
#     for i in num_str:
#         res_str += str(int(i)**2)
#     return int(res_str)

# print(square_digits(9199))


# 2 - Vowel Count


# def get_count(sentence):
#     count = 0
#     vowels = ["a","e","i","o","u"]
#     for char in sentence:
#         if char in vowels:
#             count+=1
#     return count


# 3 - More than Zero?

# def corrections(x):
#     if x > 0:
#         return f"{x} is more than zero"
#     else:
#         return f"{x} is equal to or less than zero"


# 4 - leap years

# def is_leap_year(year):
#     leap = False
    
#     if year % 400 == 0:
#         leap = True
#     elif year % 4 == 0 and year % 100 != 0:
#         leap = True
    
#     return leap


# 5 - shortes word 


# def find_short(s):
#     return min([len(word) for word in s.split()])