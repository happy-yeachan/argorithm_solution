import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    q = deque(input().strip().split())
    cnt = 1
    while 1:
        if q[0] == max(q):
            if M == 0:
                print(cnt)
                break
            else:
                M -=1
                q.popleft()
                cnt +=1
        else:
            if M == 0:
                M = len(q)-1
            else:
                M-=1
            q.rotate(-1)    