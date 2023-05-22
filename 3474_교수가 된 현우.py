import sys
# 0이 몇개인지 구하려면 5*2개수 -> 5의 배수의 개수를 구하면 됨.
# 25같은 경우는 5x5로 2개의 5로 만들어져 있어서 2개여서 0을 2개 만들 수 있음
n = int(sys.stdin.readline())
result = []
for i in range(n):
    a = int(sys.stdin.readline())
    tmp = 5
    cnt = 0
    while tmp <= a:
        cnt += a //tmp
        tmp *= 5
    result.append(cnt)

for i in result:
    print(i)
