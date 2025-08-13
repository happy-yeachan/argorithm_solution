def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_remain = 0  # 배달해야 할 남은 상자 수
    p_remain = 0  # 수거해야 할 남은 상자 수
    
    # 가장 먼 집부터 거꾸로 탐색
    for i in range(n - 1, -1, -1):
        d_remain += deliveries[i]
        p_remain += pickups[i]
        
        # 해당 위치의 배달/수거가 남아있으면 이동
        while d_remain > 0 or p_remain > 0:
            d_remain -= cap
            p_remain -= cap
            answer += (i + 1) * 2  # 왕복 거리
    
    return answer
