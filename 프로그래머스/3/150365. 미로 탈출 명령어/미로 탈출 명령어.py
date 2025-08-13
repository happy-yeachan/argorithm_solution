def solution(n, m, x, y, r, c, k):
    # 최소 이동 거리 계산
    min_dist = abs(r - x) + abs(c - y)
    if min_dist > k or (k - min_dist) % 2 == 1:
        return "impossible"
    
    # 사전순으로 가장 빠른 순서
    dirs = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    path = []

    for _ in range(k):
        for move, dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            # 범위 체크 먼저
            if not (1 <= nx <= n and 1 <= ny <= m):
                continue
            
            remain = k - len(path) - 1
            dist = abs(r - nx) + abs(c - ny)
            
            # 남은 거리로 도달 가능 & 짝수 조건
            if dist <= remain and (remain - dist) % 2 == 0:
                path.append(move)
                x, y = nx, ny
                break
    
    return "".join(path)
