#16953 A->B 
#B를 가지고 A를 만들어보자

a, b = map(int, input().split())
i = [3, 5, 7, 9]  #B의 1의 자리가 이 숫자면 문제의 조건으로는 만들 수 없음
cnt = 1
while(a <= b):
    if (a == b):
        print(cnt)
        exit()
 
    if (b%10 in i):   #B의 1의 자리가 이 숫자면 문제의 조건으로는 만들 수 없음
        print('-1') 
        exit()   
    
    if (b%10 == 1):
        b = int(b/10)    #1제거
        cnt += 1
    else:
        b = b/2 
        cnt += 1

print('-1')   # a==b를 거치지 않고 while문을 빠져나오면 -1 출력 