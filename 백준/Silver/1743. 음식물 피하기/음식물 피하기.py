import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

li = [[0]*M for x in range(N)]
visit = [[0]*M for x in range(N)]
mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(K):
    r, c = map(int, input().split())
    li[r-1][c-1] = 1

def bfs(i, j):
    size = 1
    q = deque()
    q.append((i, j))
    while q:
        y, x = q.popleft()
        for m in mv:
            ny = y + m[0]
            nx = x + m[1]
            if 0<=ny<N and 0<=nx<M:
                if li[ny][nx] == 1 and visit[ny][nx] == 0:
                    q.append((ny, nx))
                    visit[ny][nx] = 1
                    size+=1
    return size

result = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and li[i][j] == 1:
            result = max(bfs(i, j), result)

print(result-1)