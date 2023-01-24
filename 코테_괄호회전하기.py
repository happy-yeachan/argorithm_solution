def solution(s):
    s = list(s)  #문자열을 리스트화
    sum = len(s)
    if (len(s)%2 ==1):  #홀수이면 올바른 괄호 문자열이 안됨 -> 미리 판별
        return 0
    for i in range(0, len(s)):
        tmp = [] # 괄호의 짝을 판별할 스택 구현
        try:
            for j in range(0, len(s)):
                if(s[j] == ")"):
                    y = tmp.pop()
                    if(y == "("):
                        continue
                    else:
                        sum -= 1
                        break
                elif(s[j] == "}" or s[j] == "]"):
                    y = tmp.pop()
                    if(ord(y)+2 == ord(s[j])):  #아스키코드로 한번에 판별
                        continue
                    else:
                        sum -= 1
                        break
                else:
                    tmp.append(s[j])
        except IndexError:
            sum -= 1

        s.append(s.pop(0))
    return sum

print(solution('}]()[{'))