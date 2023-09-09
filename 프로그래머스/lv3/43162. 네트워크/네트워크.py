def solution(n, computers):
    global chk
    answer = 0
    chk = [False]*n
    for i in range(n):
        if not chk[i]:
            chk[i] = True
            answer += 1
            dfs(i, computers, n)
    return answer

from collections import deque
def dfs(idx, computers, n):
    q = deque()
    q.append(idx)
    while q:
        now = q.popleft()
        for i in range(idx+1, n):
            if computers[now][i] == 1 and computers[i][now] == 1 and not chk[i]:
                chk[i] = True
                q.append(i)