import sys

input = sys.stdin.readline

N, M = map(int,input().split())

d = {}
result = []
for i in range(N):
    tmp = input()
    d[tmp] = 0

for j in range(M):
    tmp = input()
    if tmp in d:
        result.append(tmp)
result.sort()
print(len(result))
for z in result:
    print(z[:-1])
