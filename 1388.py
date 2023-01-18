#1388번: 바닥 장식 (파이썬)
a, b = map(int, input().split())
count = 0
array = []

for i in range(a):
    array.append(list(input()))  #2차원 배열 만들기

for i in range(b):
    for j in range(a):
        if(i==b-1 and array[j][i] == '-' or j==a-1 and array[j][i] == '|'):   
        #오른쪽 끝, 아래 끝부분 처리
            count += 1
        elif(array[j][i] == '|' and array[j+1][i] != '|' or array[j][i] == '-' and array[j][i+1] != '-'):  
        # 열: '-'에서 '|'로 바뀌는 부분,  행: '|'에서 '-'로 바뀌는 부분 카운트
            count += 1
print(count)