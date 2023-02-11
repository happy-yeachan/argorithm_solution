#11561_징검다리
#더하는 값이 1씩 증가하는 등차수열을 합을 다리의 계수보다 커지는 지점까지 구함
#거기서 그 지점에서 한타임 전의 수를 구하면 최대 개수를 구해질 것 같음
#한타임 전 수에서 겅중 뛰어버리면 될듯?

# import sys
# a = int(sys.stdin.readline())
# bridge = []
# for _ in range(a):
#     bridge.append(int(sys.stdin.readline()))

# for i in bridge:
#     if (i == 1):
#         print(1)
#         continue
#     a, p = 0, 1
#     while a!=1:  #등차수열 계산
#         a += p
#         p += 1
#     if (i-a) < p:
#         print(p-2)
#     else:
#         print(p-1)
# -> 시간초과...

import sys
a = int(sys.stdin.readline())
bridge = []
for _ in range(a):
    bridge.append(int(sys.stdin.readline()))

for i in bridge:
    a = int((2*i+(1/4))**(1/2)-1/2)
    if (i - (a*(a+1)/2) > (a+1)):
        print(a+1)
    elif((i - (a*(a+1)/2) <= (a+1))):
        print(a)