import math
i = int(input())
for j in range(i):
    x1, y1, r1 , x2, y2, r2 = map(int,input().split())
    rs = r1 if r1 < r2 else r2
    rl = r1 if r1 > r2 else r2
    r3 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if r3 == 0:#두 원의 원점이 같을 경우
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif ((r3 < r2) or (r3 < r1)): #((r2 * 2 < r1) or (r1 * 2 < r2)) and 
        #r의 반지름 길이가 다른 r의 지름 길이보다 긴 상태 (원안에 다른원이 존재하는 경우)
        if(rs + r3 > rl):
            print(2)
        elif(rs + r3 < rl):
            print(0)
        else:
            print(1)
            
    else:#평균
        if r3 > (r1 + r2):
            print(0)
        elif r3 < (r1 + r2):
            print(2)
        elif r3 == (r1+r2):
            print(1)
            
            