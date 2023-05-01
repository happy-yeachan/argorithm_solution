import sys
import math

#에라토스테네스의 체
def sosu(n):
    array = [True for i in range(n + 1)] 

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1

    return sum(array) #True의 개수 총 합

li = []
flag = True
while(flag == True):
    n = int(sys.stdin.readline())
    if (n != 0):
        li.append(n)
    else:
        flag = False

for i in li:
    print(sosu(i*2)-sosu(i)) # 2n 범위의 소수의 개수에서 n범위의 소수의 개수를 빼줌