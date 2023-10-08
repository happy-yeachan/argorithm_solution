import sys

input = sys.stdin.readline

case = int(input())
result = []
for i in range(case):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        result.append(max(sticker)[0])

    else:
        dp = [[0]*n for _ in range(2)]

        dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
        dp[0][1], dp[1][1] = dp[1][0] + sticker[0][1], dp[0][0] + sticker[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

        result.append(max(max(dp[0]), max(dp[1])))

for i in result:
    print(i)