import sys
input = sys.stdin.readline

def back(idx, li_sum):
    global cnt
    if li_sum == s:
        cnt +=1
    for i in range(idx, n):
        li_sum += li[i]
        back(i+1, li_sum)
        li_sum -= li[i]

n, s = map(int, input().split())
li =  list(map(int, input().split()))
cnt = 0
li_sum = 0
back(0, li_sum)

if s == 0:
    cnt -=1

print(cnt)