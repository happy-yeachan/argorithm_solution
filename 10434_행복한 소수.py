import sys
import math


def is_prime_number(x): # 소수 판별
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
    if(is_prime_number(li[i]) == False or li[i] == 1): #소수 먼저 판별
        li[i] = str(i+1) + " " + str(li[i]) + " NO"
        continue # 소수가 아니면 아니면 아래 코드 무시하고 다음으로
    a = 0
    for s in str(li[i]): # 각 자리수 제곱해서 a에 저장
        a += int(s)**2
    while(1): # a가 1인지 이전에 나왔던 수 인지 확인하며 둘 다 아니면 다시 각 자리수 제곱 후 더함 반복
        if a == 1:
            li[i] = str(i+1) + " " + str(li[i]) + " YES"
            break
        elif a in tmp:  # 무한반복 방지
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