# 분할 정복
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]              
result = 0     
result_zero = 0
def color_paper(y, x, n):  # n = 종이의 너비 y, x = 종이의 왼쪽 위 좌표
    global result, result_zero
    color = 0
    for i in range(y, y+n):
        for j in range(x, x+n):
            if paper[i][j] == 1:
                color += 1
    if color == n**2:
        result += 1
        return
    elif color == 0:
        result_zero += 1
        return
    else:
        for index in [(y, x), (y+n//2, x), (y, x+n//2), (y+n//2, x+n//2)]:
            color_paper(index[0], index[1], n//2)
color_paper(0,0,N)
print(result_zero)
print(result)
        
            
    