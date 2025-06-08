import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    tmp = int(input())
    if tmp != 0:
        heapq.heappush(heap, (abs(tmp), tmp))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
