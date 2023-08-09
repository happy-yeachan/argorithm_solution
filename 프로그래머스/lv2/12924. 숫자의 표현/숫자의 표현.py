def solution(n):
    answer = 0
    for i in range(1, n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp > n:
                break
            elif tmp == n:
                print("answer", answer)
                answer +=1
                break
            
    return answer