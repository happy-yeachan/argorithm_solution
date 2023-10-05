import sys, heapq
input = sys.stdin.readline

n = int(input())

learn = [list(map(int, input().split())) for _ in range(n)]
learn.sort(key= lambda x : (x[1], x[0]))

cnt = 1
end_time = learn[0][1]
for i in range(1, n):
    if learn[i][0] >= end_time:
        cnt += 1
        end_time = learn[i][1]
print(cnt)
