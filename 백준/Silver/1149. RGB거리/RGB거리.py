import sys

input = sys.stdin.readline

n = int(input())

li = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]

dp[0] = li[0]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2])+li[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2])+li[i][j]
        else:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1])+li[i][j]

print(min(dp[n-1]))