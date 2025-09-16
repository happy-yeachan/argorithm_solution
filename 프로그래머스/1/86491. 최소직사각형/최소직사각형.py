def solution(sizes):
    sizes = [(max(w,h), min(w,h)) for w,h in sizes]
    
    max_w = max(w for w,h in sizes)
    max_h = max(h for w,h in sizes)
    
    return max_w * max_h