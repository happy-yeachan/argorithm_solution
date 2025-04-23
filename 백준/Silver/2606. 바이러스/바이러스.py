import sys
from collections import deque



input = sys.stdin.readline

node_cnt = int(input())
line_cnt = int(input())

lines = [list(map(int, input().strip().split())) for _ in range(line_cnt)]

nodes = [0 for x in range(node_cnt+1)]
nodes[1] = 1

q = deque()
q.append(1)

while q:
    tmp = q.popleft()
    for line in lines:
        if line[0] == tmp and nodes[line[1]] == 0:
            q.append(line[1])
            nodes[line[1]] = 1
        elif line[1] == tmp and nodes[line[0]] == 0:
            q.append(line[0])
            nodes[line[0]] = 1

print(sum(nodes)-1)