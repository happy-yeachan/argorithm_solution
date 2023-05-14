import sys
import math


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
    


p = int(sys.stdin.readline())
li = []

for _ in range(p):
    a, b = map(int, sys.stdin.readline().split())
    li.append(b)



for i in range(len(li)):
    tmp = []
    if(is_prime_number(li[i]) == False or li[i] == 1):
        li[i] = str(i+1) + " " + str(li[i]) + " NO"
        continue
    a = 0
    for s in str(li[i]):
        a += int(s)**2
    while(1):
        if a == 1:
            li[i] = str(i+1) + " " + str(li[i]) + " YES"
            break
        elif a in tmp:
            li[i] = str(i+1) + " " + str(li[i]) + " NO"
            break
        else:
            tmp.append(a)
            b = a
            for s in str(a):
                   a += int(s)**2      
            a -= b

for i in li:
    print(i)