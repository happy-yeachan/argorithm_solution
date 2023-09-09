import sys
input = sys.stdin.readline

n = int(input())

danzi = [list(map(int, input().strip())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
result = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# dfs 구현
def dfs(y, x):
    global each
    check[y][x] = 1
    each += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if check[ny][nx] == 0 and danzi[ny][nx] == 1:
                dfs(ny, nx)

for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and danzi[i][j] == 1:
            each = 0
            dfs(i, j)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)