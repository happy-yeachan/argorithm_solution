import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = [ int(input()) for _ in range(n)]

n -= 1
cnt = 0
while k != 0:
    if li[n] > k:
        n -=1
    else:
        cnt += k // li[n]
        k %= li[n]


print(cnt)