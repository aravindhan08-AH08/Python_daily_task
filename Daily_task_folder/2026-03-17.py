# Question 1
def matrix_transpose(mat):
    if len(mat) == 0:
        return "Invalid Input"
    
    else:
        rows = len(mat)
        cols = len(mat[0])
        
        result = []
        i = 0
        
        while i < cols:
            new_row = []
            j = 0
            
            while j < rows:
                new_row.append(mat[j][i])
                j = j + 1
            
            result.append(new_row)
            i = i + 1
        
        return result


print(matrix_transpose([[1,2],[3,4],[5,6]]))
print(matrix_transpose([[7,8],[9,10],[11,12]]))

# Question 2
def find_duplicates(nums):
    if len(nums) == 0:
        return "Invalid Input"
    
    else:
        n = len(nums)
        result = []
        i = 0

        while i < n:
            j = i + 1

            while j < n:
                if nums[i] == nums[j]:
                    result.append(nums[i])
                    break
                j = j + 1

            i = i + 1

        return result


print(find_duplicates([4,3,2,7,8,2,3,1]))
print(find_duplicates([1,1,2,3,4]))
print(find_duplicates([1,2,3,4]))