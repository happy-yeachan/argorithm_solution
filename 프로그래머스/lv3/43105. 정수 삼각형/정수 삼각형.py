def solution(triangle):
    # 양 사이드는 미리 구한다
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
        
    # 나머지 dp배열도 채워준다
    for i in range(2, len(triangle)):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] +=  max(triangle[i-1][j-1], triangle[i-1][j])
    return max(max(triangle))