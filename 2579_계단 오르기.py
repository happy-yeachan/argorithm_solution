# 한 번에 한 계단 or 두 계단

import sys

n = int(sys.stdin.readline())
stair = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    stair.append(tmp)

#이걸 생각 못했네.., 멍처이인가
if len(stair)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(stair))

else:
    dp = [0] * n
    dp[0] = stair[0]  # 첫 계단까지 최대값
    dp[1] = stair[0] + stair[1] # 두번째 계단까지 최대값 (연속 밟기)
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2]) #3번째 계단까지 최대값
    for i in range(3, n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i]) # dp점화식

    print(dp[n-1]) # 마지막 계단까지의 최대값