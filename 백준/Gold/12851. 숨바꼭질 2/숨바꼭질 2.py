import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

chk = [0]*100001
cnt = 0
q = deque([n])
min_step = 100000

while q:
    tn = q.popleft()
    if chk[tn] > min_step:
        break
    if tn == k:
        if chk[k] <= min_step: 
            min_step = chk[k]
            cnt += 1

    for i in (tn-1, tn+1, tn*2):
        if 0<=i and i<=100000:
            if (chk[i] == 0):
                chk[i] = chk[tn] + 1
                q.append(i)
            elif(chk[i] == chk[tn] + 1): #다른 곳에서도 올 수 있으니
                q.append(i)


print(min_step)
print(cnt)