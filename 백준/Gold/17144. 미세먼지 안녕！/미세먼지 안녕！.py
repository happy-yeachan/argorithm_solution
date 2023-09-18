import sys
input = sys.stdin.readline

def spread_dust(matrix):
    new_matrix = [[0] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if matrix[r][c] > 0:
                spread_amount = matrix[r][c] // 5
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] != -1:
                        new_matrix[nr][nc] += spread_amount
                        matrix[r][c] -= spread_amount
    
    for r in range(R):
        for c in range(C):
            matrix[r][c] += new_matrix[r][c]

def operate_air_purifier(matrix, air_purifier):
    upper_cleaner, lower_cleaner = air_purifier
    upper_cleaner_row = upper_cleaner[0]
    lower_cleaner_row = lower_cleaner[0]
    
    # Upper air purifier
    for r in range(upper_cleaner_row - 1, 0, -1):
        matrix[r][0] = matrix[r - 1][0]
    for c in range(C - 1):
        matrix[0][c] = matrix[0][c + 1]
    for r in range(upper_cleaner_row):
        matrix[r][C - 1] = matrix[r + 1][C - 1]
    for c in range(C - 1, 0, -1):
        matrix[upper_cleaner_row][c] = matrix[upper_cleaner_row][c - 1]
    matrix[upper_cleaner_row][1] = 0
    
    # Lower air purifier
    for r in range(lower_cleaner_row + 1, R - 1):
        matrix[r][0] = matrix[r + 1][0]
    for c in range(C - 1):
        matrix[R - 1][c] = matrix[R - 1][c + 1]
    for r in range(R - 1, lower_cleaner_row, -1):
        matrix[r][C - 1] = matrix[r - 1][C - 1]
    for c in range(C - 1, 0, -1):
        matrix[lower_cleaner_row][c] = matrix[lower_cleaner_row][c - 1]
    matrix[lower_cleaner_row][1] = 0

def total_dust_amount(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total + 2

R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

air_purifier = []
for r in range(R):
    if matrix[r][0] == -1:
        air_purifier.append((r, 0))

for _ in range(T):
    spread_dust(matrix)
    operate_air_purifier(matrix, air_purifier)

result = total_dust_amount(matrix)
print(result)
