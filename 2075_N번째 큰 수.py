# 메모리 제한 12mb == 12000kb == 12,000,000byte
# 파이썬에서 int 4byte
# n의 최대 크기는 1,500  -> 만들어지는 리스트의 최대 크기는 2,250,000 = (1,500^2) -> 54,000,000,000byte
# 모든 n x n의 배열을 다 저장하면 메모리가 초과된 고로 아래의 코드는 메모리가 초과되는 코드..;;

# import sys

# n = int(sys.stdin.readline())

# li = []

# for _ in range(n):
#     li.append(list(map(int, sys.stdin.readline().split())))

# for i in range(n-1):
#     tmp = 1
#     m = li[n-1].index(max(li[n-1]))
#     while(1):
#         if(li[n-1][m] == li[n-1-tmp][m]):
#             tmp += 1
#         else:
#             li[n-1][m] = li[n-1-tmp][m]
#             break   


# print(max(li[n-1]))


#우선순위 큐를 이용해 메모리 줄여보기
import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:  #현재 확인하고 있는 숫자가 우선순위 큐의 최솟값보다 작은 경우는 무시해버리기 큐에 (큐에 요소가 n개보다 많을 경우에)
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])