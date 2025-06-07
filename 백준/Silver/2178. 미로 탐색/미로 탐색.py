from collections import deque

N, M = map(int, input().split())

miro = [list(map(int, list(input().strip()))) for _ in range(N)]

q= deque()
q.append((0,0))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<N and 0<=nx<M:
            if miro[ny][nx] == 1:
                miro[ny][nx] = miro[y][x] + 1
                q.append((ny, nx))

print(miro[N-1][M-1])