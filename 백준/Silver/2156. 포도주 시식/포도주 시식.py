import sys

# 입력
n = int(sys.stdin.readline())
jan = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    jan.append(tmp)

if n<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(jan))
else:
    dp = [0] * n
    dp[0] = jan[0]
    dp[1] = jan[0]+jan[1]
    dp[2] = max(jan[0]+jan[1], jan[1]+jan[2], jan[0]+jan[2])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-3]+jan[i-1]+jan[i], dp[i-2]+jan[i]) # dp점화식
    print(dp[n-1])

# 이거 계단오르기 문제랑 똑같은거 같은데 좀 다르네
# 계단 오르기는 무조건 마지막 계단을 밟아야 하는데 이건 그냥 최대 값을 찾는 문제
# 그래서 dp의 맨 마지막 요소와 그 앞 요소를 비교하는 것임