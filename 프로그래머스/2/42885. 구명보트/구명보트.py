# 오름차순 정렬
# 가장 큰 수랑 가장 작은 수를 더했을 때 100보다 작으면 둘이 같이 태우기
# 100보다 커지면 가장 큰 수는 혼자 타라고 하면 될듯?

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while(len(people) > 0):
        big = people.pop()
        if len(people) == 0:
            answer += 1
        elif ((people[0]+big) <= limit):
            people.popleft()
            answer += 1
        else:
            answer += 1
    return answer

