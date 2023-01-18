#9461번: 파도반 수열
result = []
count = int(input())
for i in range(count):                  #입력된 수 만큼 반복
    num = int(input())     
    a = [1]*3                           #a[0~2]는 모두 1로 초기화
    if(num>3):
        for j in range(3, num):
            a.append(a[j-3]+a[j-2])     # 수열의 규칙이 a[n-3] + a[n-2] = a[n]을 만족 (n이 3 이상일 때)
    result.append(a.pop())              #맨 마지막에 저장된 값을 꺼내 결과 리스트에 넣어줌
for i in range(count):                  # 출력
    print(result[i])