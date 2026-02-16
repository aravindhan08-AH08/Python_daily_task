def finding_indices(nums, target):  
    if len(nums) == 0:
        return 'invalid input'
    else:
        result = [] # output list
# two pointer
    left = 0
    right = len(nums) - 1
    while left <= right:
# print(left,right)
# finding the temporary sum of two numbers
        temp = nums[left] + nums[right]
        if temp < target:
            left = left + 1
        if temp > target:
            right = right - 1
        else:
            return [left,right]

print(finding_indices([2,11,15,7], 9))
# print(finding_indices([11,2,7,15],9))
print(finding_indices([2,7,11,15], 9))
print(finding_indices([3,3], 6))


def finding_vowel(s,c):
    first = c[0]
    last = c[1]
    f = 0
# for i in range(0,len(s),+1):
#     if s[i] == first:
#         f = i
#     if s[i] == last:
#         l = i
    count = 0
    vowels = "aeiouAEIOU"
    for j in range(f,+1):
        if s[j] in vowels:
            count = count +1
    print(count)

finding_vowel("abcideouf",["d","f"])
finding_vowel("aeibcfou",["b","c"])

# Some error this code so anyone fix reach out to me.

def remove_consecutive(nums):
    if len(nums) == 0:
        return 'invalid input'
    else:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] != nums[right]:
                left +=1
                nums[left] = nums[right]
            right +=1
        result = []
        for i in range(0, left+1,+1):
            result.append(nums[i])
        print(result)

remove_consecutive([1,1,2,2,2,3,1,1])