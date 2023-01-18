#2872
#순서대로 정렬된 수들을 찾고 그 나머지를 순서대로 뽑아서 순서대로 쌓으면 될듯
import sys
n = int(sys.stdin.readline())
nl = []
cn = 1

for _ in range(n):
    nl.append(int(sys.stdin.readline()))    # 배열로 입력

big_index = nl.index(max(nl))      #최대값의 인덱스
big = max(nl)-1                     #비교할 변수 선언

for i in range(big_index, -1, -1):               #최대값부터 내림차순 
    if(nl[i] == big):
        cn += 1
        big -= 1
                       
print(n-cn)