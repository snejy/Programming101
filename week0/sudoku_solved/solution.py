def sudoku_solved(sudoku):
    revsudoku = rev(sudoku)
    return magic_square(sudoku,45) and magic_square(revsudoku,45)
    
def magic_square(matrix,k):
    for i in range(0,len(matrix) - 1):
        if k != sum(matrix[i]) != sum(matrix[i + 1]):
            return False
    else:
        return True

def rev(matrix):
    sum = []
    sums = []
    for i in range(0,len(matrix)):
        for j in range (0, len(matrix)):
            sum.append(matrix[j][i])
        sums.append(sum)
        sum = []
    return sums
