import sys

pt = []

for i in range(3):
    pt.append(list(map(int, sys.stdin.readline().split())))

result = (pt[0][0]*pt[1][1]+pt[1][0]*pt[2][1]+pt[2][0]*pt[0][1]) - (pt[1][0]*pt[0][1]+pt[2][0]*pt[1][1]+pt[0][0]*pt[2][1])
#신발끈공식 쓰면 바로 풀림
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)