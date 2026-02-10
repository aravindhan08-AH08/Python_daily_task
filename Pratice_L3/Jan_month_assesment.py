# Level 3 
# Question 1
def print_first_last(s):
    if len(s) == 0:
        print("Empty String")
    else:
        print(s[0])
        print(s[-1])

print_first_last("Aravindhan") # Output A n

# Question 2
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"

    for char in s:
        if char in vowels:
            count += 1

    print(count)

count_vowels("rhythm") #output 0
count_vowels("education") # output 5

# Question 3
def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Python is full fun")) # Output 4
print(count_words("I Love Programming in JavaScript")) # Output 5


# Question 4
def new_string(s):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in s:
        if char not in vowels:
            result += char
    
    return result

print(new_string("education"))
print(new_string("academy"))

# Question 5
s = input()

result = ""

for char in s:
    if not char.isdigit():
        result += char

print(result)

# Question 6
# s = input()

# words = s.split()
# result = []

# for word in words:
#     result.append(word[::-1])

# print(" ".join(result))

# Question 7
word = input()
letter = input()

count = 0

for char in word:
    if char == letter:
        count += 1

print(count)

# Question 8
def check_palindrome(word):
    i = 0
    j = len(word) - 1
    
    while i < j:
        if word[i] != word[j]:
            print("No")
            return
        i += 1
        j -= 1
    
    print("Yes")

# Example Tests
check_palindrome("level")
check_palindrome("section")

# Question 9
numbers = list(map(int, input().split()))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

diff_list = []
for num in numbers:
    diff_list.append(num - average)

print(diff_list)

# Lot: 2
# Question 1
numbers = eval(input())

squared_list = []

for num in numbers:
    squared_list.append(num * num)

print(squared_list)

# Question 2
numbers = eval(input())
target = int(input())

count = 0

for num in numbers:
    if num == target:
        count += 1

print(count)

# Question 3
# numbers = eval(input())

# result = []

# for num in numbers:
#     if num < 0:
#         result.append(0)
#     else:
#         result.append(num)

# print(result)

# Question 4
numbers = eval(input())

count = 0

for num in numbers:
    if num > 50:
        count += 1

print(count)

# Question 5
numbers = eval(input())

if len(numbers) == 0:
    print("List is empty")
else:
    result = numbers[0] + numbers[-1]
    print(result)

# Question 6
items = eval(input())

for i in range(len(items)):
    print("Index", i, items[i])

# Question 7
numbers = eval(input())

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("even_sum =", even_sum, ", odd_sum =", odd_sum)

# Question 8
x = eval(input())

for i in range(len(x)):
    if x[i] < 0:
        x[i] = 0

print(x)

# Question 9
main_list = eval(input())
sublist = eval(input())

found = False

for i in range(len(main_list) - len(sublist) + 1):
    match = True
    for j in range(len(sublist)):
        if main_list[i + j] != sublist[j]:
            match = False
            break
    if match:
        found = True
        break

print(found)

# Model 2 Strings
# Question 1
s1 = input()
s2 = input()

if len(s1) != len(s2):
    print(False)
else:
    if s2 in (s1 + s1):
        print(True)
    else:
        print(False)

# Question 2
# Count how many students passed (≥ 40)
scores = eval(input())

count = 0
for score in scores:
    if score >= 40:
        count += 1

print(count)

# Question 3
# Count how many products cost more than 1000
prices = eval(input())

count = 0
for price in prices:
    if price > 1000:
        count += 1

print(count)

# Question 4
# Print cities with more than 6 letters
cities = eval(input())

for city in cities:
    if len(city) > 6:
        print(city)