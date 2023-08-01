import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li = [list(map(int,input().split())) for _ in range(n)]

chk = [[False]*m for _ in range(n)]

cnt = 0
max_area = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    area = 1
    q=[(y,x)]
    while q:
        ey, ex = q.pop()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if li[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny, nx))
                    area += 1
    return area



for i in range(n):
    for j in range(m):
        if not chk[i][j] and li[i][j] == 1:
            chk[i][j] = True
            cnt+=1
            area = bfs(i,j)
            max_area = max(max_area, area)

print(cnt)
print(max_area)