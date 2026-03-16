# Question 1
def maxProfit(prices):
    if len(prices) <= 0:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))

# Question 2
def compress_string(s):
    if len(s) == 0:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result


s = "aabcccccaaa"
print(compress_string(s))

# Question 3
def groupAnagrams(strs):
    result = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in result:
            result[key] = []

        result[key].append(word)

    return list(result.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))