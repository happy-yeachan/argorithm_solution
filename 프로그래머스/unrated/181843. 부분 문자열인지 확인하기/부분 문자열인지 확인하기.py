def solution(my_string, target):
    answer = 0
    # my_string이라는 문자열이 target문자열에 존재한다면
    if target in my_string: 
        # answer를 1로 지정
        answer = 1
    # 위 조건문에 걸리지 않았으면 0, 걸렸으면 1 반환
    return answer