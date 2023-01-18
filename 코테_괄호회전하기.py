import re
def solution(s):
    s = list(s)
    sum = 0
    if (len(s)%2 ==1):
        return 0
    for i in range(0, len(s)):
        test = ''.join(s)
        # test = test.replace("()", "").strip()
        # test = test.replace("{}", "").strip()
        # test = test.replace("[]", "").strip()
        new_text = re.sub("[]", "", test)
        print(new_text)
        if (len(new_text) == 0):
            sum += 1
        s.append(s.pop(0))
    return sum

print(solution('[](){}'))