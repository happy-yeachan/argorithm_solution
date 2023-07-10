import sys, heapq
# 입력
n = int(sys.stdin.readline())
classT = []
classR = []

for i in range(n): classT.append(list(map(int, sys.stdin.readline().split())))

classT.sort(key = lambda x:x[0])
heapq.heappush(classR, classT[0][1])

for i in range(1, n):
    if classR[0] <= classT[i][0]:
        heapq.heappop(classR)
        heapq.heappush(classR, classT[i][1])
    else:
        heapq.heappush(classR, classT[i][1])

print(len(classR))