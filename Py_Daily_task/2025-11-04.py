# # Given two lists — one with last month’s marks and another with this month’s marks.
# # print how many students improved their scores.
# # Input:
# # last_month_score = [45, 60, 70, 55, 80]
# # this_month_score = [50, 58, 75, 65, 78]
# # Output: 3
# # Explanation: here students number 1, 3, and 4 are improved in the scores

# # Answer :

# last_month_score = [45, 60, 70, 55, 80]
# this_month_score = [50, 58, 75, 65, 78]

# count = 0

# for i in range(len(last_month_score)):
#     if this_month_score[i] > last_month_score[i]:
#         count += 1

# print(count)

# # 2. Convert all spaces in a given sentence into - (without using in-built functions).
# # ```python
# # Input: "Learn Python Easily"
# # Output: "Learn-Python-Easily"
# # ```

# # Answer :

# sentence = "Learn Python Easily"
# result = ""

# for char in sentence:
#     if char == " ":
#         result += "-"
#     else:
#         result += char

# print(result)


# # 3. Find Index of an Element (Without using index() or any in-built methods) Write a program to find the index position of a given number manually using loops.
# # python
# # Input:
# # numbers = [11, 22, 33, 44, 55]
# # search = 33
# # Output: 2


# numbers = [11, 22, 33, 44, 55]
# search = 33

# index_position = -1 

# for i in range(len(numbers)):
#     if numbers[i] == search:
#         index_position = i
#         break

# print(index_position)



# # You are given two lists:
# # One list shows the gender of each student ('M' for male, 'F' for female).
# # The other list shows their marks in the same order.
# # Write a Python program to:
# # Find the average marks of male students.
# # Find the average marks of female students.
# # Print "Male <average>" if male students have the higher average, or "Female <average>" if female students have the higher average.

# # For example:
# # Test
# # find_higher_average(['M','F','M','F','M','F','M'],
# #                     [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0]) 

# # Output: Male 85.0

# # find_higher_average(['M','F','M','F','M','F','M'],
# #                     [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])

# # Output: Female 80.0


# def find_higher_average(gen_list, marks_list):
#     male_sum = 0
#     female_sum = 0
#     male_count = 0
#     female_count = 0

#     for i in range(len(gen_list)):
#         if gen_list[i] == 'M':
#             male_sum += marks_list[i]
#             male_count += 1
#         else:
#             female_sum += marks_list[i]
#             female_count += 1

#     male_avg = male_sum / male_count
#     female_avg = female_sum / female_count

#     if male_avg > female_avg:
#         print("Male", male_avg)
#     else:
#         print("Female", female_avg)

# Question 1:
# Write a Python program to check if a given string is a Pangram or not.
# A Pangram is a sentence that contains every letter of the English alphabet (a–z) at least once. 
# The check should be case-insensitive, meaning both uppercase and lowercase letters are treated the same.

# Test Case 1:
# Input:The quick brown fox jumps over the lazy dog
# Output:True

# Explanation:
# The input string contains all the letters from ‘a’ to ‘z’, so it is a Pangram.

# Test Case 2:
# Input: The quick brown fox jumps over the dog
# Output: False

# Explanation:
# The input string is missing some letters (‘l’, ‘z’, and ‘y’), so it is not a Pangram.


sentence = input("Enter one sentence: ")
sentence = sentence.lower()
words  = "abcdefghijklmnopqrstuvwxyz"
count=0
for i in words:
    if i in sentence:
        count+=1
if count==26:
    print(True)
else:
    print(False)        


     