import sys
from collections import deque
n = int(sys.stdin.readline())

dice = list(map(int,sys.stdin.readline().split()))

#주사위 하나만 사용할 경우
if n == 1:
    print(sum(dice)-max(dice))
    exit()

# case1: 변 부분 구하기
case1 = 0
if n>=3:
    case1 = min(dice)*((n-2)*(n-1)*4+(n-2)**2)

tmp = deque(dice)


# case2: 꼭지점 부분 구하기
tmp.pop()
tmp.popleft()
min_side = min([tmp[0]+tmp[1], tmp[1]+tmp[3], tmp[3]+tmp[2], tmp[2]+tmp[0]])

if dice[0] >= dice[5]: case2 = (min_side+dice[5]) * 4
else: case2 = (min_side+dice[0]) * 4

# case3: 모서리 부분 구하기

if dice[0] >= dice[5]: tmp1 = min(tmp)+dice[5]
else: tmp1 = min(tmp)+dice[0]

if tmp1 >= min_side: case3 = min_side * ((n-2)*8+4)
else: case3 = tmp1 * ((n-2)*8+4)

print(case1+case2+case3)