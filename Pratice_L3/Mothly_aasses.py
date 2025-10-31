# Print all elements in a list
# Input: numbers = [10, 20, 30, 40]
# Output:
# 10
# 20
# 30
# 40

# numbers = [10, 20, 30, 40, 36, 45, 67, 3, 5]
# for i in range(0,len(numbers)):
#     if numbers[i] % 2 != 0:
#         print(numbers[i])


# 2. Print only even numbers
# Input: [1, 2, 3, 4, 5, 6]
# Output: 2 4 6

# num = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(num)):
#     if num[i] % 2 == 0:
#         print(num[i])

# 3. Print only odd numbers
# Input: [10, 11, 12, 13]
# Output: 11 13

# num = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(num)):
#     if num[i] % 2 != 0:
#         print(num[i])

# 4. Find the sum of all numbers
# Input: [5, 10, 15]
# Output: 30

# num = [5, 10, 15]
# count = 0
# for i in range(0, len(num)):
#     if num[i] % 2 != 0:
#         count += num[i]
# print(count)

# 5. Find the largest number (without max function)
# Input: [4, 9, 2, 7]
# Output: 9
 
# numbers = [4, 9, 2, 7]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest number:", largest)


# 6. Count how many numbers are greater than 10
# Input: [5, 15, 25, 2, 9]
# Output: 2

# num = [5, 15, 25, 2, 9, 10]
# count = 0
# for i in range(0, len(num)):
#     if num[i] <= 10:
#         count +=1
# print(count)

# 7. Add 5 to each number and print new list
# Input: [1, 2, 3]
# Output: [6, 7, 8]

# num =  [1, 2, 3]
# for i in range(0, len(num)):
#     print(num[i]+5)

# 8. Count how many times 0 appears in the list
# Input: [0, 1, 0, 2, 3, 0]
# Output: 3

# num = [0, 1, 0, 2, 3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1]
# count = 0
# for i in range(0, len(num)):
#     if num[i] == 0:
#         count +=1
# print(count)

# 9. Print elements at even index positions
# Input: [10, 20, 30, 40, 50]
# Output: 10 30 50

# num = [10, 20, 30, 40, 50]
# for i in range(0, len(num)):
#     if i % 2 == 0:
#         print(num[i])

# 10. Compare two lists and print matching items (by index)
# list1 = [1, 2, 3, 4]
# list2 = [1, 5, 3, 7]
# Output:
# 1
# 3

# Noo

# 11. Count spaces
# Count how many spaces are in a sentence.
# Input: "Python is fun"
# Output: 2

text = "Python is fun"

count = 0
for char in text:
    if char == " ":
        count += 1
print("Number of spaces:", count)

# 12. Count characters except spaces
# Count total number of non-space characters.
# Input: "I like Python"
# Output: 10

# 13. Print characters at even positions
# Print only characters that are in even index positions.
# Input: "Python"
# Output: "Pto"

# 14. Create new string by skipping vowels
# Print all characters except vowels.
# Input: "Education"
# Output: "dctn"