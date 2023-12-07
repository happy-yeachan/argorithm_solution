def solution(age):
    answer = ''
    age = str(age)
    for i in range(len(age)):
        answer += chr(int(age[i])+97)
    
    return answer