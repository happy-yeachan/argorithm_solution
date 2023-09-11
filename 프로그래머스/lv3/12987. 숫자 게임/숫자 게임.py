def solution(A, B):
    A.sort()
    B.sort()
    idx = 0
    cnt = 0
    for i in B:
        if A[idx]<i:
            cnt +=1
            idx +=1
    return cnt