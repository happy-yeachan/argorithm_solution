from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        price = q.popleft()
        t = 0
        for i in q:
            t += 1
            if price > i:
                break 
        answer.append(t)        
    return answer