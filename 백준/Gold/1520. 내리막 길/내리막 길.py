import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

li = [list(map(int, input().split()))for _ in range(N)]
dp = [[-1] * M for _ in range(N)]


dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def dfs(y, x):
    if y == N-1 and x == M-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x] 

    dp[y][x] = 0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=ny<N and 0<=nx<M:
            if li[ny][nx] < li[y][x]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0,0))