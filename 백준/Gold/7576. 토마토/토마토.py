import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

tomato = [list(map(int,input().split())) for _ in range(m)]
chk = [[0]*n for _ in range(m)]
cnt = 0
m_cnt = 0
q = deque([])
# dfs 시작점 찾기
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            q.append((i,j))
        elif tomato[i][j] == -1:
            m_cnt +=1


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while q:
    ey, ex = q.popleft()
    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0<=ny<m and 0<=nx<n: # 범위를 벗어나는지 확인
            if tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[ey][ex] + 1
                q.append((ny, nx))
d = 0
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        d = max(tomato[i][j], d)


print(d-1)