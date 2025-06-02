# (0,0) 출발
# 범위 안에서만 이동
# 오른쪽 아래로만 이동 가능
# 가장 오른쪽 가장 아래 도착 = 승리
# 이동가능 수는 밟고있는 칸의 수 만큼 무조건 이동

import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[False]*N for _ in range(N)]
    visited[i][j] = True

    while q:
        y, x = q.popleft()

        if y == N-1 and x == N-1:
            return True 

        if game[y][x] <= 0:
            continue

        ny = y + game[y][x]
        if ny < N and not visited[ny][x]:
            visited[ny][x] = True
            q.append((ny, x))

        nx = x + game[y][x]
        if nx < N and not visited[y][nx]:
            visited[y][nx] = True
            q.append((y, nx))

    return False


N = int(input())

game = [list(map(int, input().split())) for _ in range(N)]


if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")