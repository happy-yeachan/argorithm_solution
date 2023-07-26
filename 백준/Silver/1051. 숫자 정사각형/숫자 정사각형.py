import sys


n,m = map(int,sys.stdin.readline().split())
tmp = [list(map(int,sys.stdin.readline().strip())) for i in range(n)]
max_width = min(n,m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(max_width): # 정사각형이니까 더 짧은 부분을 가지고 탐색
            if (i+k) < n and (j+k) < m and (tmp[i][j] == tmp[i+k][j] == tmp[i][j+k] == tmp[i+k][j+k]): 
                # 탐색 범위가 처음 지정한 n x m을 넘어가지 않는지 판단 후 꼭지점의 값이 같은지 또 판단
                answer = max(answer, (k+1)**2)
                # 모두 탐색하며 가장 큰 값을 찾는다
print(answer)