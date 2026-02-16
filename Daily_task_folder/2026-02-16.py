# Question 1
def contains_duplicates(nums):
    if len(nums) == 0:
        return "invalid input"
    else:
        # output = []
        # for i in range(0,len(nums),+1):
        #     if nums[i] not in output:
        #         output.append(nums[i])
        #         print(nums)
        #         print(output)

        # if len(nums) == len(output):
        #     return False
        # else:
        #     return True

        #approach 2
        for i in range(0,len(nums), +1):
            for j in range(i+1, len(nums),+1):
                if nums[i] == nums[j]:
                    return True
            return False


print(contains_duplicates([1,2,3,1]))

# Question 2
def bowling_stats(pitch):
    if len(pitch) == 0:
        return "Invalid Input"
    else:
        result = 0
        max_count = 0
        for i in range(0,len(pitch), +1):
            curr_count = 0
            for j in range(0,len(pitch[i]), +1):
                if pitch[i][j] == "W":
                    curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
                result = i
        print(result+1)

bowling_stats([
    ["B","B","B"],
    ["B","W","B"],
    ["W","B","B"],
    ["B","W","B"],
    ["W","W","B"]
])
