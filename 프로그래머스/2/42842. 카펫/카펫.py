def solution(brown, yellow):
    sum = brown + yellow
    answer = []
    # 세로의 길이는 무조건 3보다 크니까 3부터 탐색 시작
    for i in range(3, sum):
        if sum % i == 0:
            # 가로 = sum//i-2
            # 새로 = i-2
            if (sum//i-2)*(i-2) == yellow:
                answer.append(sum//i)
                answer.append(i)
                break
    return answer