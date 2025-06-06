from collections import deque

M, N, H = map(int, input().split())

box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]


# 익은 토마토 위치 탐색
tomatos = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                tomatos.append((i,j,k))


# bfs 진행
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while tomatos:
    z, y, x = tomatos.popleft()
    for i in range(6):
        nz  = z + dz[i]
        ny  = y + dy[i]
        nx  = x + dx[i]
        if 0<=nz<H and 0<=ny<N and 0<=nx<M:
            if box[nz][ny][nx] == 0:
               box[nz][ny][nx] = box[z][y][x] + 1
               tomatos.append((nz, ny, nx))


# 0이 있으면 -1 없으면 최대값 도출
result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, box[i][j][k])

print(result-1)