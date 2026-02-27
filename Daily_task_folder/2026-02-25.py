def sum_last_num(arr):
    if len(arr) < 3:
        return "Invalid Input"
    else:
        result = []
        sum = 0
        l = len(arr)
        for i in range(l-3, l):
            sum += arr[i]
        for j in range(len(arr)):
            result.append(arr[j]-sum)
        return result
    
print(sum_last_num([95, 85, 75, 12, 11]))
print(sum_last_num([95, 23, 11]))

def rearrange(num):
    if len(num) == 0 or len(num) > 10:
        return "Invalid Input"
    else:
        output = []
        for i in range(0, len(num), +1):
            temp = num[i]
            output.append(num[temp])
        return output
    
print(rearrange([4,0,2,1,3]))
print(rearrange([]))

def unique_usernames(arr):
    count = {}
    result = []

    for name in arr:
        if name not in count:
            count[name] = 0
            result.append("Verified")
        else:
            count[name] += 1
            result.append(name + str(count[name]))

    return result


# Test
print(unique_usernames(["abc", "aab", "abc", "aba"]))
print(unique_usernames(["user", "user", "user"]))