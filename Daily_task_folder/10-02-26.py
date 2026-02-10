# Tic Tac Toe Game So ithu Row wise check panrom and Check Column wise and corner to corner mathiri check panrom 
# Care fully use this code and u try and use the code don't copy paste
def tic_tac_toe(gameboard):
    if len(gameboard) == 0:
        return "invalid input"

    row = len(gameboard)
    col = len(gameboard[0])

    # row wise check
    for i in range(row):
        temp = set(gameboard[i])
        if len(temp) == 1:
            return f"{list(temp)[0]} is winner"

    # column wise check
    for j in range(col):
        temp = set()
        for i in range(row):
            temp.add(gameboard[i][j])
        if len(temp) == 1:
            return f"{list(temp)[0]} is winner"

    # right diagonal check (00, 11, 22)
    temp = set()
    for i in range(row):
        temp.add(gameboard[i][i])
    if len(temp) == 1:
        return f"{list(temp)[0]} is winner"

    # left diagonal check (02, 11, 20)
    temp = set()
    for i in range(row):
        temp.add(gameboard[i][col - 1 - i])
    if len(temp) == 1:
        return f"{list(temp)[0]} is winner"

    return "No winner"


print(
    tic_tac_toe(
        [
            ["O", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "X"],
        ]
    )
)

# Another think is u Try More Test Case and u call it me tell i'm walkthrough