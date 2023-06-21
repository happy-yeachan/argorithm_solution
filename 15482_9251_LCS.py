def lcs(m1, m2):
    dp = [0] * len(m2)
    for i in range(len(m1)):
        max_dp = 0
        for j in range(len(m2)):
            if max_dp < dp[j]:
                max_dp = dp[j]
            elif m1[i] == m2[j]:
                dp[j] = max_dp + 1
    print(max(dp))

m1 = input()
m2 = input()
lcs(m1, m2)
