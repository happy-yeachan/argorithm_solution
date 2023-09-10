import sys
input=sys.stdin.readline

def back(cnt, idx):
    global minv
    if cnt == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(i, n):
                if visit[i] and visit[j]:
                    start += (li[i][j] + li[j][i])
                elif not visit[i] and not visit[j]:
                    link += (li[i][j] + li[j][i])
        minv = min(minv, abs(start - link))
        return
    
    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            back(cnt+1,i)
            visit[i] = False



n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

minv = int(1e9)
visit = [False]*n
back(0, 0)
print(minv)