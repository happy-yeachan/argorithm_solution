T = int(input())
li = [int(input()) for _ in range(T)]

max_n = max(li)  
dp = [0] * (max_n + 1)

dp[1:4] = [1, 2, 4]

for i in range(4, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for n in li:
    print(dp[n])