import sys
input = sys.stdin.readline

brackets = input()

st = []

tmp = 1
ans = 0

if (len(brackets)-1)%2 !=0:
    print(0)
    exit()

for i in range(len(brackets)):
    # 올바르지 않은 입력일 시 0 출력
    if (brackets[i] == ')' and (not st or st[-1] != '(')) or (brackets[i] == ']' and (not st or st[-1] != '[')):
        print(0)
        exit()
    elif brackets[i] == '(':
        st.append(brackets[i])
        tmp *= 2
    elif brackets[i] == '[':
        st.append(brackets[i])
        tmp *= 3
    elif brackets[i] == ')':
        if brackets[i-1] == '(':
            ans += tmp
            tmp //= 2
        else:
            tmp //= 2
        st.pop()
    elif brackets[i] == ']':
        if brackets[i-1] == '[':
            ans += tmp
            tmp //= 3
        else:
            tmp //= 3
        st.pop()

print(ans)