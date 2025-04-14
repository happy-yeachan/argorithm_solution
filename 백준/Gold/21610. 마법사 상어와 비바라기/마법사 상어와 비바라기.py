#  (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# d 방향으로 s칸 이동
# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

# 처음 구름 (0-index로!)
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 8방향 (←, ↖, ↑, ↗, →, ↘, ↓, ↙)
mv = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
      (0, 1), (1, 1), (1, 0), (1, -1)]

# 대각선 방향만
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for _ in range(M):
    d, s = map(int, input().split())

    # 구름 이동
    new_clouds = []
    for x, y in clouds:
        nx = (x + mv[d-1][0] * s) % N
        ny = (y + mv[d-1][1] * s) % N
        new_clouds.append((nx, ny))
        li[nx][ny] += 1  # 비 내리기
    clouds = new_clouds

    # 물 복사 버그 (대각선 체크)
    for x, y in clouds:
        cnt = 0
        for dx, dy in diagonal:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and li[nx][ny] > 0:
                cnt += 1
        li[x][y] += cnt

    # 구름 생성
    prev_clouds = set(clouds)  # 구름이 있었던 자리 기억
    clouds = []

    for i in range(N):
        for j in range(N):
            if li[i][j] >= 2 and (i, j) not in prev_clouds:
                clouds.append((i, j))
                li[i][j] -= 2

# 결과 계산
print(sum(map(sum, li)))
