#코테_게임 맵 최단거리
#깊이우선

from collections import deque

# dfs 사용
def bfs(x,y,n,m,maps,visit):
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                # 상하좌우로 움직였을 때 maps의 크기를 벗어나면 가지 못하도록 함
                continue
            if maps[nx][ny] and not visit[nx][ny]: #한 번도 방문하지 않은 경우 
                visit[nx][ny] = 1 
                maps[nx][ny] = maps[x][y]+1 # 방문 횟수를 올려줌
                queue.append((nx,ny)) # 현재 위치 변경

    if maps[n-1][m-1] == 1:
        # 1이면은 목표에 도달하지 못함. (한 번이라도 방문하면 2가 됨)
        return -1

    return maps[n-1][m-1]

def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열
    visited = [[0]*m for i in range(n)]
    visited[0][0]=1
    return bfs(0,0,n,m,maps,visited)