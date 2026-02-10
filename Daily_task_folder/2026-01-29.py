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