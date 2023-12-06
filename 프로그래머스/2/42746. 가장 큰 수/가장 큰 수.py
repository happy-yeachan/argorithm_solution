def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x : x*3)
    answer = int(''.join(numbers))
    return str(answer)