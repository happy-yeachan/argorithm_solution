def solution(n, w, num):
    H = (n + w - 1) // w               # 전체 층
    r = (num + w - 1) // w             # num의 층
    p = (num - 1) % w + 1
    c = p if r % 2 else w - p + 1      # 열 위치

    def row_len(t):
        if t < H: return w
        return n - w * (H - 1) or w    # 마지막 층

    ans = 1
    for t in range(r + 1, H + 1):
        lt = row_len(t)
        if (t % 2 and c <= lt) or (t % 2 == 0 and c >= w - lt + 1):
            ans += 1
    return ans
