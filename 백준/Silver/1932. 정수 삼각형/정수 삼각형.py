import sys

n = int(sys.stdin.readline())

triangle = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    triangle.append(tmp)

# 음 이걸 트리 형태라고 봐야하나?
# 한 노드에 부모가 두 개인 트리가 있었나.,.?
# 1차원 배열에서는 규칙을 찾기가 힘들다..
# 2차원 배열로 다시 생각

# 각 노드의 위치를 기준으로 dp 설정
dp = triangle.copy()


for i in range(1, n):
    # 양옆은 그냥 바로 위의 노드 값을 가져와 더한 값임(부모가 하나여서) 
    dp[i][0] += dp[i-1][0]
    dp[i][i] += dp[i-1][i-1]
    for j in range(1,i):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))