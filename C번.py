class sul:
    def __init__(self, name, x): 
        self.name = name
        self.__x= x
    def addx(self, x):
        self.x += x

num = int(input())
nlist = []
for _ in range(num):
    name, x = input().split()
    if name in nlist:
        nlist[nlist.index(name)+1].__x += x
    else:
        nlist.append(name)
        nlist.pop = sul(name, x)
        
print(nlist)