import sys
import re

num = int(sys.stdin.readline())
result = []
for _ in range(num):
    n = list(sys.stdin.readline())
    n.pop()
    count_R = n.count('R')
    count_D = len(n) - count_R
    i = int(sys.stdin.readline())
    li = list(map(int,((re.findall(r'\d+', sys.stdin.readline())))))
    if(count_D > i): #빼는게 총 수보다 맞은면 error추가
        result.append("error")
    elif(count_D == i):
        result.append([])
    else:
        a = 0
        for j in n:
            if(j == 'R' and a == 0): a = 1
            elif(j == 'R' and a != 0): a = 0
            elif(j == 'D' and a != 0):
                li.pop()
            else: li.pop(0)
        if (count_R % 2 != 0): 
            li.reverse()
        result.append(li)

for i in result:
    print(i)
