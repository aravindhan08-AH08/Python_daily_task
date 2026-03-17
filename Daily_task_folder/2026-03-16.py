# Question 1
def longest_palindrome(word):
    if len(word) == 0:
        return "Invalid Input"
    
    else:
        n = len(word)
        longest = ""

        i = 0
        while i < n:
            
            # odd length palindrome
            left = i
            right = i
            
            while left >= 0 and right < n and word[left] == word[right]:
                if (right - left + 1) > len(longest):
                    longest = word[left:right+1]
                left = left - 1
                right = right + 1

            # even length palindrome
            left = i
            right = i + 1
            
            while left >= 0 and right < n and word[left] == word[right]:
                if (right - left + 1) > len(longest):
                    longest = word[left:right+1]
                left = left - 1
                right = right + 1

            i = i + 1

        return longest


print(longest_palindrome("babad"))
print(longest_palindrome("cbba"))
print(longest_palindrome("pqr"))
print(longest_palindrome("abaxyzzyxf"))

# Question 2
def sort_colors(nums):
    if len(nums) == 0:
        return "Invalid Input"
    
    else:
        count0 = 0
        count1 = 0
        count2 = 0

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                count0 = count0 + 1
            elif nums[i] == 1:
                count1 = count1 + 1
            else:
                count2 = count2 + 1
            i = i + 1

        i = 0
        
        # fill 0s
        while count0 > 0:
            nums[i] = 0
            i = i + 1
            count0 = count0 - 1

        # fill 1s
        while count1 > 0:
            nums[i] = 1
            i = i + 1
            count1 = count1 - 1

        # fill 2s
        while count2 > 0:
            nums[i] = 2
            i = i + 1
            count2 = count2 - 1

        return nums


print(sort_colors([2,0,2,1,1,0]))