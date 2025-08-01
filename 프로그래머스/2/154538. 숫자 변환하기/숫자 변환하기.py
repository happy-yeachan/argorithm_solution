from collections import deque
def solution(x, y, n):
    check = [-1 for i in range(y+1)]
    check[x] = 0
    q= deque()
    q.append(x)
    while(q):
        now = q.popleft()
        if now == y:
            return check[now]
        for i in [now+n, now*2, now*3]:
            if i <= y and check[i] == -1:
                check[i] = check[now] + 1
                q.append(i)
    
    return -1