import sys
input = sys.stdin.readline
n, k = map(int, input().split())

tmp = [[0,0]]
DP = [[0] * (k+1) for _ in range(n+1)]
#x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어줌

for _ in range(n):
    tmp.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = tmp[i]
        if j >= w:
            DP[i][j] = max(DP[i-1][j] , DP[i-1][j-w] + v)
                    #= max(dp[이전 물건][현재 가방 무게], 현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게])
        else:
            DP[i][j] = DP[i-1][j]
            #w보다 작으면 위의 값을 그대로 가져옴

print(DP[i][k])