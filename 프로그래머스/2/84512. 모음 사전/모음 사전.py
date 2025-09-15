def solution(word):
    order = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    # 5^4, 5^3, 5^2, 5, 1
    weights = [781, 156, 31, 6, 1]
    ans = 0
    for i, ch in enumerate(word):
        ans += order[ch] * weights[i] + 1
    return ans
