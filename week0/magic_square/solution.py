def magic_square(matrix):
    for i in range(0,len(matrix)-1):
        if sum(matrix[i])==sum(matrix[i+1])==sum_diagonal(matrix):
            matrix.reverse()
            if sum_diagonal(matrix)==sum(matrix[i]):
                return True
    else:
        return False

def sum_diagonal(matrix):
    sum=0
    for i in range(0,len(matrix)):
        sum= sum + matrix[i][i]
    return sum
