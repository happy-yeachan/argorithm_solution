def solution(brown, yellow):
    sum = brown + yellow
    answer = []
    # 세로의 길이는 무조건 3보다 크니까 3부터 탐색 시작
    for i in range(3, sum):
        if sum % i == 0:
            if (sum//i-2)*(i-2) == yellow:
                answer.append(sum//i)
                answer.append(i)
                break
                #a b를 찾은 후 위 식을 만족하는 b a도 찾아버리기 때문에 바로 break시켜줌
    return answer


print(solution(10,2))