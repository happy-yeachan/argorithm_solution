from functools import cmp_to_key

def compare(x, y):
    # 두 수를 붙였을 때 더 큰 쪽이 앞에 오도록 비교
    if x + y > y + x:
        return -1  # x가 앞으로
    elif x + y < y + x:
        return 1   # y가 앞으로
    else:
        return 0   # 동일

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    result = ''.join(numbers)
    return '0' if result[0] == '0' else result
