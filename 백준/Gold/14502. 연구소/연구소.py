import sys
input = sys.stdin.readline

# 백트래킹
def back(wall):
    if wall == 3:
        tmp_li = [mat[:] for mat in li]
        bfs(tmp_li)
        return

    for i in range(n):
        for j in range(m):
            if li[i][j] == 0:
                li[i][j] = 1
                back(wall+1)
                li[i][j] = 0

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

# bfs진행
from collections import deque
def bfs(tmp_li):
    global result
    q = deque()

    for i in range(n):
        for j in range(m):
            if li[i][j] == 2:
                q.append((i,j))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny <n and 0<=nx<m:
                if tmp_li[ny][nx] == 0:
                    tmp_li[ny][nx] = 2
                    q.append((ny, nx))
    count = check_safe(tmp_li)
    result = max(result, count)

def check_safe(tmp_li):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_li[i][j] == 0:
                cnt += 1
    return cnt


n, m = list(map(int, input().split()))
li = [list(map(int, input().split())) for _ in range(n)]

result = 0

back(0)

print(result)
