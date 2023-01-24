#코테_괄호 회전하기
#스택활용

def solution(s):
    s = list(s)  #문자열을 리스트화
    sum = len(s)
    if (len(s)%2 ==1):  #홀수이면 올바른 괄호 문자열이 안됨 -> 미리 판별
        return 0
    for i in range(0, len(s)):
        tmp = [] # 괄호의 짝을 판별할 스택 초기화
        try:
            for j in range(0, len(s)):      #닫는 괄호면 이전에 여는 괄호가 있었는지 판별
                if(s[j] == ")"):    #닫는괄호 1
                    y = tmp.pop()
                    if(y == "("):
                        continue
                    else:
                        sum -= 1
                        break
                elif(s[j] == "}" or s[j] == "]"):   #닫는 괄호 2
                    y = tmp.pop()
                    if(ord(y)+2 == ord(s[j])):  
                    #아스키코드로 한번에 판별 {}, []는 아스키코드로 변환했을 때 서로 2만큼 차이가 남
                        continue
                    else:
                        sum -= 1
                        break
                else:        # 여는 괄호면 tmp에 추가
                    tmp.append(s[j])
        except IndexError:    #인덱스에러가 발생하면 여는괄호 없이 닫는 괄호가 접근했다는 뜻 -> sum이 하나 줄어든다.
            sum -= 1

        s.append(s.pop(0))
    return sum