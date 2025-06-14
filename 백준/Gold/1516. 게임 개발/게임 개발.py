import sys
from collections import deque
input = sys.stdin.readline

# 순서ㅇ가 있는 작업 -> 위상 정렬을 사용하자
# 그래프 배열, 진입 차수 배열, 비용 배열, DP 배열 
N = int(input())
graph = [[] for i in range(N)]
indegree = [0] * N
cost = [0] * N
DP = [0] * N


for i in range(N):
    tmp = list(map(int, input().split()))[:-1]
    cost[i] = tmp[0]
    for j in tmp[1:]:
        graph[j-1].append(i)
        indegree[i] += 1

q = deque()

for i in range(N):
    if indegree[i] == 0:
        DP[i] = cost[i]
        q.append(i)

while q:
    n = q.popleft()
    
    for i in graph[n]:
        indegree[i] -= 1
        # 선행 건물 중 가장 오래 걸리는 시간 + 나의 건축 시간을 찾아야함
        DP[i] = max(DP[i], DP[n] + cost[i])
        
        if not indegree[i]: q.append(i)

for i in range(N):
    print(DP[i])