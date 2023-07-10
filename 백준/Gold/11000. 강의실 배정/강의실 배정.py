import sys, heapq

classT = []
classR = []

# 입력
n = int(sys.stdin.readline())
for i in range(n): classT.append(list(map(int, sys.stdin.readline().split())))

# 수업 시작 시간을 기준으로 정렬
classT.sort(key = lambda x:x[0])

# 가장 먼저 시작하는 수업 푸쉬
# 힙큐를 사용하여 자동으로 정렬되게 설정
heapq.heappush(classR, classT[0][1])

for i in range(1, n):
    # 수업이 끝난 강의실이 있으면 거기 사용
    if classR[0] <= classT[i][0]:
        heapq.heappop(classR)
        heapq.heappush(classR, classT[i][1])
    else:
        heapq.heappush(classR, classT[i][1])

print(len(classR))
