def solution(angle):
    answer = 0
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle == 180:
        return 4
    elif angle > 90:
        return 3
    return answer