def solution(n, left, right):
    tmp = []
    cnt = 0
    # 수 채움과 동시에 1차원 배열로 표현
    for i in range(left, right+1):
        a = i//n+1
        b = i%n+1
        if a >= b:
            tmp.append(a)
        else:
            tmp.append(b)

    return tmp