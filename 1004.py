import math

def isInclude(x1,y1,r1, x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    if distance < r1:
        return True
    else:
        return False
T = int(input())

for t in range(T):
    xs, ys, xf, yf = map(int, input().split())
    amount = int(input())
    answer = 0
    for a in range(amount):
        x, y, z = map(int, input().split())
        include1 = isInclude(x,y,z,xs,ys)
        include2 = isInclude(x,y,z,xf,yf)
        if (include1 and include2) or (not(include1) and not(include2)):
            continue
        else:
            answer += 1
            continue
            
    print(answer)