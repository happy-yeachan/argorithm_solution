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


# 등차수열의 합공식 이용
# n(n+1)/2
import sys
a = int(sys.stdin.readline())
bridge = []
for _ in range(a):
    bridge.append(int(sys.stdin.readline()))

for i in bridge:
    a = int((2*i+(1/4))**(1/2)-1/2)   
    # n(n+1)/2 = i 를 n에 대하여 정리하여 n값을 구하고 int형으로 저장
    # 정수로 딱 나오면 그대로 출력하면 되고
    # 소수점이 생겼을 때 아래 두가지 경우로 판별
    if (i - (a*(a+1)/2) > (a+1)):
    # 소수점 구간이 등차수열로 따졌을 때 나올 항 보다 크면 한번에 건너면 되니까 + 1
        print(a+1)
    elif((i - (a*(a+1)/2) <= (a+1))):
    # 소수점 구간이 등차수열로 따졌을 때 나올 항 보다 작으면 한칸 뒤로 갔다가 한번에 건너기
        print(a)