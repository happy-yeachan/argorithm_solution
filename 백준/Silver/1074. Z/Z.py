n, r, c = map(int, input().split())


tmp = 2**n
ans = 0

for i in range(n):
    tmp //= 2   
    if r < tmp and c >= tmp:
        ans += tmp**2
        c -= tmp
    elif r >= tmp and c >= tmp:
        ans += (tmp**2)*3
        c -= tmp
        r -= tmp
    elif r >= tmp and c < tmp:
        ans += (tmp**2)*2
        r -= tmp
    

print(ans)