N = int(input())
lst = [[' ' for _ in range(N)] for _ in range(N)]

def make_star(n, x, y, r):# n은 범위
    if n == 1:#재귀의 끝 
        lst[y][x] = r
        return
    n //= 3
    #사각형을 만드는 과정 (여기서 가운데에 해당하는 부분은 재귀의 마지막까지 빈공간을 출력하도록 한다.)
    
    make_star(n, x, y, r)
    make_star(n, x+n, y, r)
    make_star(n, x+n*2, y, r)
    
    make_star(n, x, y+n, r)
    make_star(n, x+n,  y+n, ' ')
    make_star(n, x+n*2,  y+n, r)
    
    make_star(n, x, y+n*2, r)
    make_star(n, x+n,  y+n*2, r)
    make_star(n, x+n*2,  y+n*2, r)
    
    return
make_star(N, 0, 0, '*')
for line in lst:
    print(''.join(line))