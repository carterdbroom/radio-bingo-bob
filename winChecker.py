# This is a helper function that checks if a row has been completed.
# Returns True if all number in the row are found int he lis of called numbers.
def checkRow(matrix: list[list[int]], numbersList: list[int], rowNum: int) -> bool:
    for i in matrix[rowNum]:
        if i not in numbersList:
            return False
    return True

# This is a helper function that checks if a column has been completed. 
# Returns True if all numbers in the column are found in the list of called numbers.
def checkColumn(matrix: list[list[int]], numbersList: list[int], colNum: int) -> bool:
    for i in range(6):
        if matrix[i][colNum] not in numbersList:
            return False
    return True

# This is a helper function that checks if a diagonal has been completed.
# Returns True if all numbers in the diagonal are found in the list of called numbers.
def checkDiagonal(matrix: list[list[int]], numbersList: list[int], diagNum: int) -> bool:
    if diagNum == 0:
        for i in range(6):
            if matrix[i][i] not in numbersList:
                return False
        return True
    if diagNum == 1:   
        for i in range(6):
            if matrix[5-i][i] not in numbersList:
                return False
        return True
    return False

# This is a function that checks if a single row has been completed.
# Returns True if a row, column, or diagonal is complete. 
def checkSingleWin(matrix: list[list[int]], numbersList: list[int]) -> bool:
    for i in range(2):
        if checkDiagonal(matrix, numbersList, i):
            return True
    for i in range(6):
        if checkRow(matrix, numbersList, i):
            return True
        if checkColumn(matrix, numbersList, i):
            return True
    return False

# This is a function that checks if two rows have been completed.
# Returns True if two of any combination of either a row, column, or diagonal is complete.
def checkDoubleWin(matrix: list[list[int]], numbersList: list[int]) -> bool:
    count = 0
    for i in range(2):
        if checkDiagonal(matrix, numbersList, i):
            count += 1
        if count == 2:
            return True
    for i in range(6):
        if checkRow(matrix, numbersList, i):
            count += 1
            if count == 2: 
                return True
        if checkColumn(matrix, numbersList, i):
            count += 1
            if count == 2:
                return True
    return False

# This is a function that checks if an entire card is complete. 
# Returns true if all numbers on the card have been called.
def checkFullCardWin(matrix, numbersList):
    count = 0
    for i in range(6):
        if checkRow(matrix, numbersList, i):
            count += 1
    if count == 5:
        return True
    return False