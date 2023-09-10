import sys
input = sys.stdin.readline

# 부호가 올 수 있는 모든 경우의 수 백트래킹
def back(i, arr):
    global add, sub, mul, div, maxv, minv
    if i == n:
        maxv = max(maxv, arr)
        minv = min(minv, arr)
    else:
        if add > 0:
            add -= 1
            back(i+1, arr + li[i])
            add += 1
        if sub > 0:
            sub -= 1
            back(i+1, arr - li[i])
            sub += 1
        if mul > 0:
            mul -= 1
            back(i+1, arr*li[i])
            mul += 1
        if div > 0:
            div -= 1
            back(i+1, int(arr/li[i]))
            div += 1

n = int(input())
li = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

maxv = int(-1e9)
minv = int(1e9)

back(1, li[0])

print(maxv)
print(minv)