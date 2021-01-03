N = int(input())
lst = []
max_1 = 0
max_2 = 0
for _ in range(N):
    tmp = int(input())
    if max_1 < tmp:
        max_2 = max_1
        max_1 = tmp
    elif max_2 < tmp:
        max_2 = tmp
max_value = 0
miners = max_1 - max_2 + 1 if max_1 - max_2 + 1 < max_2 else max_2
for i in range(1, miners):
    one = max_1 - i
    two = max_2 - i
    r = 99999
    while r:  # 유클리드 알고리즘, 호제
        r = one % two
        one = two
        two = r
    if one > max_value:
        max_value = one
for i in range(2, max_value // 2 + 1):
    if max_value % i == 0:
        print(i, end = ' ')
print(max_value)