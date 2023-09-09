def solution(n):
    tmp1, tmp2 = 0, 1
    for i in range(n-1): tmp2, tmp1 = tmp1+tmp2, tmp2
    return tmp2%1234567


print(solution(5))