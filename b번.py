m = int(input())
an = 0
bn = 0
a, pa, b, pb = map(int, input().split())
if((a/pa) > (b/pb)):
    an,i = divmod(m,pa)
    if (i> pb):
        bn = i//pb
else:
    bn,i = divmod(m,pb)
    if (i> pa):
        an = i//pa

print(an, bn)