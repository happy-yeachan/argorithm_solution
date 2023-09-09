# 이거 자료구조때 배운 괄호 검사 응용하면 되겠는걸?
from collections import deque
def solution(s):
    tmp = []
    a = deque(s)

    if len(a)%2 != 0:
        return 0
    
    tmp.append(a.popleft())
    for i in a:
        if len(tmp) != 0 and tmp[-1] == i:
            tmp.pop()
        else: tmp.append(i)
    
    if len(tmp) == 0:
        return 1
    
    return 0

print(solution("cdcd"))