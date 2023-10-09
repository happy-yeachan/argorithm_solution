import sys
input = sys.stdin.readline

def back(idx):
    global tmp, cnt
    if tmp == s:
        cnt += 1

    for i in range(idx, n):
        tmp += li[i]
        back(i+1)
        tmp -= li[i]

n, s = map(int, input().split())

li = list(map(int, input().split()))

tmp = 0
cnt = 0
back(0)
if s == 0:
    print(cnt-1)
else:
    print(cnt)