import sys
input = sys.stdin.readline

N, L = map(int, input().split())

li = list(map(int, input().split()))
li.sort()
cnt = 1
tmp = 0
L1 = L-1
for i in range(N-1):
    tmp = li[i+1] - li[i]
    if tmp <= L1:
        L1 -= tmp
    else:
        cnt +=1
        L1 = L-1

print(cnt)
