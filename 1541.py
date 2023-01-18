f = input().split('-')      #-를 기준으로 분류
for i in range(0, len(f)):  
    a = map(int, f[i].split('+'))    #0009-0009 같은 경우 10진수는 0부터 시작하면 오류가 나서 int화 해주는 작업
    f[i] = sum(a)       # 분류된 부분을 계산

a = (sum(f)-2*f[0]) * (-1)   # 최소값 계산
print(a)