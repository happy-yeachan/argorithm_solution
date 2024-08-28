def solution(s):
    count = 0  # 이진 변환 횟수를 세기 위한 변수
    zero_count = 0  # 제거된 0의 총 개수를 세기 위한 변수
    
    while s != "1":
        # 1. 현재 문자열에서 0을 모두 제거하고, 제거된 0의 개수를 센다.
        zero_count += s.count('0')
        s = s.replace("0", "")
        
        # 2. 남은 문자열의 길이를 2진법으로 변환하여 새로운 s로 설정한다.
        s = bin(len(s))[2:]
        
        # 3. 이진 변환 횟수를 증가시킨다.
        count += 1
    
    return [count, zero_count]

