import heapq

def solution(operations):
    heap = []
    for i in operations:
        # 삽입 삭제 분리
        a, b = i.split()

        # 삽입은 heapq를 통해 자동 정렬
        if a == "I":
            heapq.heappush(heap, int(b))

        # 삭제
        else:
            # 빈 배열이면 무시
            if len(heap) == 0:
                continue
            # 최댓값
            elif int(b) == 1:
                heap.pop()
            # 최솟값
            else:
                heapq.heappop(heap)
    # 빈 배열이면 0,0 반환
    if not heap:
        return [0, 0]
    # 최댓값 최솟값 반환
    else:
        return [max(heap), min(heap)]