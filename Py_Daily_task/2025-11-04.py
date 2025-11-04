# Given two lists — one with last month’s marks and another with this month’s marks.
# print how many students improved their scores.
# Input:
# last_month_score = [45, 60, 70, 55, 80]
# this_month_score = [50, 58, 75, 65, 78]
# Output: 3
# Explanation: here students number 1, 3, and 4 are improved in the scores

# Answer :

last_month_score = [45, 60, 70, 55, 80]
this_month_score = [50, 58, 75, 65, 78]

count = 0

for i in range(len(last_month_score)):
    if this_month_score[i] > last_month_score[i]:
        count += 1

print(count)

# 2. Convert all spaces in a given sentence into - (without using in-built functions).
# ```python
# Input: "Learn Python Easily"
# Output: "Learn-Python-Easily"
# ```

# Answer :

