import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 2차원 배열로 그림 입력
paint = [list(input())[:-1] for _ in range(n)]

# 방문처리를 위한 배열 선언
check = [[0]*n for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x, color):
    q= deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and paint[ny][nx] == color:
                check[ny][nx] = 1
                q.append((ny, nx))

def RG_dfs(y, x, color):
    q= deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if color == 'B':
                if 0<=ny<n and 0<=nx<n and check[ny][nx] == 1 and paint[ny][nx] == color:
                    check[ny][nx] = 0
                    q.append((ny, nx))
            else:
                if 0<=ny<n and 0<=nx<n and check[ny][nx] == 1 and (paint[ny][nx] == 'R' or paint[ny][nx] == 'G'):
                    check[ny][nx] = 0
                    q.append((ny, nx))


no_RG_cnt = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            check[i][j] = 1
            color = paint[i][j]
            dfs(i,j, color)
            no_RG_cnt += 1

RG_cnt = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 1:
            check[i][j] = 0
            color = paint[i][j]
            RG_dfs(i,j, color)
            RG_cnt += 1


print(no_RG_cnt, RG_cnt)