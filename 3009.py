import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
dic_x = {}
dic_y = {}
result = ''
for i in [x1,x2,x3]:
    try: dic_x[i] += 1
    except: dic_x[i] = 1
for i in [y1,y2,y3]:
    try: dic_y[i] += 1
    except: dic_y[i] = 1
for x, r in dic_x.items():
    if r == 1:
        result += str(x)
result += ' '
for y, r in dic_y.items():
    if r == 1:
        result += str(y)
print(result)