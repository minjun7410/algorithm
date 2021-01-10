# 분할 정복

N = int(input())
image = [[int(i) for i in input()] for _ in range(N)]
result = ''
def quad_tree(y, x, n):
    global result
    count = 0
    for i in range(y, y+n):
        for j in range(x, x+n):
            if image[i][j] == 1:
                count += 1
    if count == n**2:
        result += str(1)
        return
    elif count == 0:
        result += str(0)
        return
    else:
        result += '('
        for index in [(y, x), (y, x+n//2), (y+n//2, x), (y+n//2, x+n//2)]:
            quad_tree(index[0], index[1], n//2)
        result += ')'
quad_tree(0, 0, N)
print(result)