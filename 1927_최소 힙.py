import sys
import heapq
n = int(sys.stdin.readline())
heap = []
result = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if (tmp==0):
        if (len(heap)==0):
            result.append(0)
        else:
            result.append(heapq.heappop(heap)) #최소힙의 헤드를 가져와 result에 넣어줌 
    else:
        heapq.heappush(heap, tmp) #입력받은 값을 최소힙 형태로 push

for i in result:
    print(i)