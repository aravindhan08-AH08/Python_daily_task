# Question 1
def matrix_group(mat):
    if len(mat) == 0:
        return "Invalid Input"
    
    else:
        n = len(mat)
        i = 0
        j =0
        while i < n:
            i = j
            while j < n:
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
                j = j + 1
            i = i + 1
        return mat
print(matrix_group([ [10,20,30],[40,60,70], [80,90,100]]))

# Question 2
# Question
def right_max(arr):
    if len(arr) == 0:
        return "Invalid Input"
    
    else:
        n = len(arr)
        i = 0
        result = []

        while i < n:
            j = i + 1
            max_val = -1

            while j < n:
                if arr[j] > max_val:
                    max_val = arr[j]
                j = j + 1

            result.append(max_val)
            i = i + 1

        return result


print(right_max([17, 18, 5, 4, 6, 1]))
print(right_max([1,2,3,4,5]))
print(right_max([10]))
print(right_max([4,7,1,3,2]))