import sys
input = sys.stdin.readline

# 음 그냥 모든 점에서 십자가가 되는지 안되는지 판단해야할듯?
# 근데 출력 순서가 안나와있네
# 아 *로 십자가를 만들 수 있냐 없냐가 요지가 아니였네
# 십자가로 입력 리스트의 *을 다 만들 수 있는지 보는거였넹
N, M = map(int, input().split())

li = [list(input().strip()) for _ in range(N)]
check = [[0]*M for _ in range(N)]

# 십자가 판별
def cross(y, x):
    size = 1
    while 1:
        for dy, dx in [(0,size), (size,0), (0,-size), (-size,0)]:
            ny = y + dy
            nx = x + dx
            if not(0 <= ny < N and 0 <= nx < M) or li[ny][nx] != '*':
                return
            
        stars.append((y+1,x+1,size))
        # 십자가 완성된 영역 표시
        check[y][x] = 0
        for dy, dx in [(0,size), (size,0), (0,-size), (-size,0)]:
            ny = y + dy
            nx = x + dx
            check[ny][nx] = 0

        size+=1


stars = []

# 십자가로 완료해야할 영역 표시
for i in range(N):
    for j in range(M):
        if li[i][j] == '*':
            check[i][j] = 1
# * 기준 십자가 판별 함수 호출
for i in range(N):
    for j in range(M):
        if li[i][j] == '*':
            cross(i, j)

# 십자가로 못만든 영역 확인
for i in check:
    if sum(i) != 0:
        print(-1)
        exit()

stars.sort(key=lambda x: (x[0], x[1], -x[2]))
print(len(stars))
for star in stars:
    print(*star)