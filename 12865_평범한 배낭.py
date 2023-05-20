import sys
input = sys.stdin.readline
n, k = map(int, input().split())

tmp = [[0,0]]
DP = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    tmp.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = tmp[i]
        if j >= w:
            DP[i][j] = max(DP[i-1][j] , DP[i-1][j-w] + v)
        else:
            DP[i][j] = DP[i-1][j]

print(DP[i][k])