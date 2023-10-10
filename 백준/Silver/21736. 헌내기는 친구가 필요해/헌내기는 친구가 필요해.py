import sys
input = sys.stdin.readline

from collections import deque


dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def bfs():
    cnt = 0
    q = deque()
    q.append((y, x))

    while q:
        py, px = q.popleft()
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if 0<= ny <n and 0<=nx<m:
                if li[ny][nx] == 'P':
                    cnt += 1
                if li[ny][nx] != 'X':
                    li[ny][nx] = 'X'
                    q.append((ny,nx))

    return cnt

n, m = map(int, input().split())

li = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if li[i][j] == 'I':
            x, y = j, i

result = bfs()

if result == 0:
    print("TT")
else:
    print(result)