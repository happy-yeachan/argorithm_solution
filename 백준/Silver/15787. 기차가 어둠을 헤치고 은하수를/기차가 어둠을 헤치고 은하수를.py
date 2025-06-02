import sys
input = sys.stdin.readline

N, M = map(int, input().split())

train = [[0]*20 for _ in range(N)]


for i in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
          if train[tmp[1]-1][tmp[2]-1] == 0:
               train[tmp[1]-1][tmp[2]-1] = 1
    if tmp[0] == 2:
          if train[tmp[1]-1][tmp[2]-1] == 1:
               train[tmp[1]-1][tmp[2]-1] = 0
    if tmp[0] == 3:
         train[tmp[1]-1] = [0] + train[tmp[1]-1][:-1]
    if tmp[0] == 4:
         train[tmp[1]-1] = train[tmp[1]-1][1:] + [0]

answer = set()
for i in train:
     answer.add(tuple(i))

print(len(answer))