n, k = map(int, input().split())

from collections import deque

q = deque()

for i in range(n):
    q.append(i+1)

yo = []
while q:
    for i in range(k-1):
        q.append(q.popleft())

    yo.append(q.popleft())

print('<' + ', '.join(map(str, yo)) + '>')