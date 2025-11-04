# **Level 3 Questions**
# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist
def split_string_inbuilt(sentence):
    substrings = sentence.split('-')
    for substring in substrings:
        print(substring)       
split_string_inbuilt("Emma-is-a-data-scientist")
       
       
        
def split_string_manual(sentence):
    current_substring = ""
    for char in sentence:
        if char == '-':
            print(current_substring)
            current_substring = ""
        else:
            current_substring += char
    print(current_substring)  # Print the last substring
split_string_manual("Emma-is-a-data-scientist")


# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP


def reverse_string_inbuilt(str1):
    reversed_str = str1[::-1]
    print(reversed_str)

def reverse_string_manual(str1):
    reversed_str = ""
    for char in str1:
        reversed_str = char + reversed_str
    print(reversed_str)

reverse_string_inbuilt('Python')
reverse_string_manual('Python')

# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7

def count_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in input_string:
        if char in consonants:
            count += 1
    return count



x = count_consonants('Hello World')
print(x)




# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome
# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome

sentance = "Python is awesome"
print(sentance.replace(" ", ""))


# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

def is_strong_password(password):
    special_characters = "!@#$%^&*"
    count = 0   
    for i in password:
        if i in special_characters:
            count+=1
    if len(password) >=8 and count >=1:
        print('Password is strong')
    else:
        print('Password is not strong')

is_strong_password('my@password')
is_strong_password('python123')