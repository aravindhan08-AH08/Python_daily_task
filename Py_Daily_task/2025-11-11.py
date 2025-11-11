# 1. Given an array nums and an integer K, remove the last K elements from the array and print the remaining elements.
# Test Case 1:
# Input : nums = [10, 20, 30, 40, 50]
# K = 2
# Output: [10, 20, 30]
# Test Case 2:
# Input: nums = [5, 15, 25]
# K = 5

nums = [10, 20, 30, 40, 50]
K = 2

#First vanthu check panrom ethu (invalid input) ah ella ya nu check panni next array test aagum you can check (Debug)
if K > len(nums) or K < 0:
    print("Invalid Input")
else:
    result = nums[:-K] if K != 0 else nums
    print(result)
# Output: Invalid Input

# 2. Given two lists, calculate the total count of odd numbers in each list. Print the list that contains the highest count of odd numbers.
# If the counts are the same, print "Odd counts are equal".
# Input:
# data_x = [1, 2, 3, 4, 5, 6, 7]
# data_y = [11, 22, 33, 44, 55]
# count = 0
# count_1 = 0

# for i in data_x:
#     if (i % 2 != 0):
#         count += 1
# for i in data_y:
#     if (i % 2 != 0):
#         count_1 += 1
# if (count > count_1):
#     print(data_x)
# else:
#     print(data_y)

# Output: [1, 2, 3, 4, 5, 6, 7]


# 3. Given an integer N and an array of N integers, write a program to 
# print all the integers that are divisible by their immediate previous integer in the array.

# Test Case 1:
# Input: [1, 2, 3, 6, 7]
# nums = [1, 2, 3, 6, 7]
# result = []

# for i in range(1, len(nums)):
#     if nums[i] % nums[i - 1] == 0:
#         result.append(nums[i])

# print(result)

# Output: [2, 6]

# Test Case 2:
# Input: [2, 4, 8, 16]
# nums = [2, 4, 8, 16]
# result = []

# for i in range(1, len(nums)):
#     if nums[i] % nums[i - 1] == 0:
#         result.append(nums[i])

# print(result)
# Output: [4, 8, 16]

# Test Case 3:
# Input: [5, 7, 11, 13, 17]
# nums = [1, 2, 3, 6, 7]
# result = []

# for i in range(1, len(nums)):
#     if nums[i] % nums[i - 1] == 0:
#         result.append(nums[i])

# print(result)
# Output: []