# 가장 큰 수들로 곱해야 최대값이 나옴
# s를 k로 나누고 몫들을 곱하고 나머지를 한 몫에 더해준 상태로 곱하면 가장 큰 수가 나올듯

import sys

s, k = map(int, sys.stdin.readline().split(" "))

m, n, tmp = s//k, s%k, 1

for _ in range(k):
    if n>0:
        tmp *= (m+1)
        n -= 1
    else:
        tmp *= m
    print(tmp)

