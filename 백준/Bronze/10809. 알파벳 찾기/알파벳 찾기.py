S = input()

li = [-1 for x in range(26)]

for i in range(len(S)):
    if li[ord(S[i])-97] == -1:
        li[ord(S[i])-97] = i

for j in li:
    print(j, end=' ')