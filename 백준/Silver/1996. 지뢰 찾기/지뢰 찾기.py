import sys
input = sys.stdin.readline

n = int(input())

mine = [list(map(str, input().strip())) for _ in range(n)]

result = [[0]*n for i in range(n)]

dy = [0, -1, 0, 1, -1, 1, 1, -1]
dx = [-1, 0, 1, 0, -1, 1, -1, 1]

for i in range(n):
    for j in range(n):
        if mine[i][j] != '.':
            result[i][j] = '*'
            for a in range(8):
                ny = i+dy[a]
                nx = j+dx[a]
                if 0<= ny < n and 0<=nx<n and result[ny][nx] != '*' and result[ny][nx] != 'M':
                    result[ny][nx] += int(mine[i][j])
                    if result[ny][nx] >= 10:
                        result[ny][nx] = "M"

for i in result:
    print("".join(map(str,i)))