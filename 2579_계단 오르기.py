# 한 번에 한 계단 or 두 계단

import sys

n = int(sys.stdin.readline())
stair = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    stair.append(tmp)

dp = [0] * n
dp[0] = stair[0]  # 첫 계단까지 최대값
dp[1] = stair[0] + stair[1] # 두번째 계단까지 최대값 (연속 밟기)
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2]) #3번째 계단까지 최대값
for i in range(3, n):
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

print(dp[n-1])