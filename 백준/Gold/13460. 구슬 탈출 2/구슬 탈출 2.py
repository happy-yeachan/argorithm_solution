import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
li = [list(input().strip()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = set()

for i in range(N):
    for j in range(M):
        if li[i][j] == 'R':
            rx, ry = i, j
        elif li[i][j] == 'B':
            bx, by = i, j

def move(x, y, dx, dy):
    dist = 0
    while li[x + dx][y + dy] != '#' and li[x][y] != 'O':
        x += dx
        y += dy
        dist += 1
    return x, y, dist


q = deque()
q.append((rx, ry, bx, by, 0))
visited.add((rx, ry, bx, by))

while q:
    rx, ry, bx, by, depth = q.popleft()
    if depth >= 10:
        break

    for i in range(4):
        nrx, nry, r_dist = move(rx, ry, dx[i], dy[i])
        nbx, nby, b_dist = move(bx, by, dx[i], dy[i])

        # 파란 구슬이 구멍에 빠질 경우
        if li[nbx][nby] == 'O':
            continue

        # 빨간 구슬만 구멍에 빠졌을 경우
        if li[nrx][nry] == 'O':
            print(depth + 1)
            exit()

        # 두 구슬이 같은 위치에 있다면 거리 더 긴 쪽을 한 칸 뒤로
        if nrx == nbx and nry == nby:
            if r_dist > b_dist:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))

print(-1)