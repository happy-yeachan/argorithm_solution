# 모든 문자를 돌며 현재 문자의 마지막 알파벳과 다음 문자의 첫 알파벳을 비교
# 이전에 이 문자가 사용된 적 있는지 비교

def solution(n, words):
    tmp = [words[0]]
    flag = False # 탈락자가 있는지 없는지 판단하기위한 flag
    for i in range(0, len(words)-1):
        if words[i+1] in tmp: 
            flag = True
            break # 이미 사용한 문자면 끝말잇기 종료
        else: tmp.append(words[i+1])
        l = words[i][-1]
        f = words[i+1][0]
        if l != f: 
            flag = True
            break #끝 말을 잇지 못한 경우
    # 탈락자 발생 시 result 구하기
    if flag == True:
        a, b = divmod(i+2, n) # i+2: 몇번째 순서에 탈락
        if b == 0: 
            return [n, a]
        else: 
            return [b, a+1]
    return [0,0]
