import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = []
for i in range(n):
    a = int(input())
    li.append(a)
n -= 1
cnt = 0
while k != 0:
    if li[n] > k:
        n -=1
    else:
        div = k//li[n]
        k -= li[n]*(div)
        cnt += div


print(cnt)