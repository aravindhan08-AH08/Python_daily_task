def find_palindrome(word:str):
    if len(word) == 0:
        return "Invalid Input"
    else:
        l = len(word)
        for i in range(0, l, +1):
            if word[i] == word[l-i-1]:
                return True
        return False
        
print(find_palindrome("Madam"))