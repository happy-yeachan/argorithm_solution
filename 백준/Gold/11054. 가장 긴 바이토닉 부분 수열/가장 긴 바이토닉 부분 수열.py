import sys

input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))

dp_left = [1]*n
dp_right = [1]*n

for i in range(1, n):
    for j in range(i):
        #왼쪽 dp 
        if s[i] > s[j]:
            dp_left[i] = max(dp_left[i], dp_left[j]+1)
        #오른쪽 dp
        if s[n-1-i]>s[n-1-j]:
            dp_right[n-1-i] = max(dp_right[n-1-i], dp_right[n-1-j]+1)

dp = [0]*n

for i in range(n):
    dp[i] = dp_left[i] + dp_right[i]

# 중복되게 셈을 한 수 빼기
print(max(dp)-1)
