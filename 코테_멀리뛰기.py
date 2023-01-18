#프로그래머스: 멀리뛰기
#혹시 규칙이 있을까

#1칸일때 2칸일때 ....
#1 2 3 5 8 13 여기까지 했을때는 피보나치수열인데
#그냥 함 해보자

def solution(n):
    a = [1, 2]
    
    for i in range(2, n):
        a.append(a[i-2] + a[i-1])

    answer = a[n-1] % 1234567
    return answer
#이게 되네.. ㅋㅋㅋ

def solution(n):
    cur, nex = 1, 2
    for i in range (1, n):
        cur, nex = nex, cur+nex
    return cur%1234567