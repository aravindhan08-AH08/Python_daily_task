def square_of_number(n):
    if n <= 0:
        return "Invalid Inuput"
    else:
        sum = 0
        while n >= 1:
            num = n % 10
            sum = sum + (num * num)
            n = n // 10
        return sum
        
print(square_of_number(19))

def first_non_repeat(s):
    
    for i in range(len(s)):
        count = 0
        
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        
        if count == 1:
            return s[i]
    
    return "None"


# Example
# s = input("Enter string: ")
print(first_non_repeat("aabbcde"))

def is_strong(num):

    if num <= 0:
        return "Not Strong"

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10

        # factorial logic here itself
        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        temp = temp // 10

    if total == num:
        return "Strong"
    else:
        return "Not Strong"


# num = int(input("Enter number: "))
print(is_strong(145))
print(is_strong(123))
print(is_strong(40585))

def missing(l):
    sum = 0
    max = l[0]
    for i in range(0,len(l),+1):
        if l[i]>max:
            max = l[i]
        sum = sum + l[i]
    find = max * (max + 1) // 2
    missing = find - sum
    print(missing)
missing(l = [1,2,4,5,6])

def find_add_number(arr):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        max = arr[0]
        for i in range(0, len(arr), +1):
            if arr[i] % 2 == 1:
                max = arr[i]
        return max

print(find_add_number([2,4,6,7,10,9,13]))