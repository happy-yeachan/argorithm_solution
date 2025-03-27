N = int(input())

z = [1, 0]
o = [0, 1]

for i in range(N):
    tmp = int(input())
    if tmp == 0:
        print(1, 0)
    elif tmp == 1:
        print(0, 1)
    else:
        for j in range(len(z), tmp+1):
            z.append(z[j-2] + z[j-1])
            o.append(o[j-2] + o[j-1])
        print(z[tmp], o[tmp])
