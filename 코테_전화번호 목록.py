
def solution(elements):
    elements.sort()
    for i in range(len(elements)-1):
        l = len(elements[i])
        if elements[i] == elements[i+1][:l]:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))