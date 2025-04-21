import sys
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split())

li = [list(map(int, input().strip().split())) for _ in range(N)]

mv =  [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

# 1 위치 탐색
pt = deque()
for i in range(N):
    for j in range(M):
        if li[i][j] == 1:
            pt.append((i, j))

while pt:
    y, x = pt.popleft()
    for dy, dx in mv:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if li[ny][nx] == 0:
                pt.append((ny, nx))
                li[ny][nx] = li[y][x] + 1


result = 0

for i in li:
    result = max(max(i), result)

print(result-1)