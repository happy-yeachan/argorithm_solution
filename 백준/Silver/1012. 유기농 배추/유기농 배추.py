from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if v[nx][ny] == 1:
                v[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    v = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        v[x][y] = 1

    for a in range(n):
        for b in range(m):
            if v[a][b] == 1:
                bfs(v, a, b)
                cnt += 1
    print(cnt)