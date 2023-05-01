import sys

def Bubble_Sort(data_set, n, k):       # 버블정렬 구현
    tmp = 0
    for _ in range(n-1, 0, -1):     # 맨 오른쪽에 큰수들이 박히니까 한 칸씩 줄이면서 for문이 돔.
        flag = True                 # 이미 정렬이 되어있는지 확인하기 위해 세워둔 flag
        for j in range(n-1):        # for문 안에서 j의 다음 인덱스까지 호출을 하니까 범위를 마지막에서 -1을 해줘야 에러가 나지 않음
            if (data_set[j] > data_set[j+1]):                               # 본인과 다음 인덱스의 값을 비교
                flag = False                                                # 스위치가 일어나면 정렬이 되어있지 않다는 뜻 임으로 flag를 False로 변환
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]     # 본인이 더 크면 서로 스위치
        tmp += 1
        if(flag) or tmp==k: break             # flag를 확인하여 정렬 상태를 판단, flag가 True인 상태로 나오면 for문 끝내기


n, k = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
Bubble_Sort(tmp, n, k)

for i in range(n):
    print(tmp[i],end=' ')

