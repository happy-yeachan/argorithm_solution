T = int(input())

for i in range(T):
    tmp = input()
    if len(tmp)%2 != 0:
        print("NO")
        continue
    stack = []
    for j in range(len(tmp)):
        if tmp[j] == "(":
            stack.append(tmp[j])
        elif tmp[j] == ")":
            if len(stack) == 0:
                break
            elif stack[-1] == "(":
                stack.pop()
            else:
                break
    if len(stack) == 0 and j == len(tmp)-1:
        print("YES")
    else:
        print("NO")