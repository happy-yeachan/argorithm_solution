S = input()

tmp = []

for i in range(len(S)):
    tmp.append(S[i:])

tmp = sorted(tmp)

for j in tmp:
    print(j)