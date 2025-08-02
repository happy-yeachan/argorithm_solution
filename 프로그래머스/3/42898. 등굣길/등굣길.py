def solution(m, n, puddles):
    MOD = 1000000007  # 문제 조건: 경로 수가 커질 수 있어서 나머지 연산

    # 격자 초기화 (0으로)
    grid = [[0] * m for _ in range(n)]

    # puddles 표시 (-1로 표시)
    for x, y in puddles:
        grid[y-1][x-1] = -1

    # DP 배열 초기화
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1  # 시작점

    for y in range(n):
        for x in range(m):
            if grid[y][x] == -1:  # 웅덩이면 경로 없음
                dp[y][x] = 0
                continue

            if y > 0:
                dp[y][x] += dp[y-1][x]  # 위쪽에서 오는 경로
            if x > 0:
                dp[y][x] += dp[y][x-1]  # 왼쪽에서 오는 경로

            dp[y][x] %= MOD  # 나머지 연산

    return dp[n-1][m-1]