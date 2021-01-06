N = int(input())
count_2 = 0
count_5 = 0
for i in range(1, N+1):
    while i:
        if i % 2 == 0:
            i //= 2
            count_2 += 1
            continue
        elif i % 5 == 0:
            i //= 5
            count_5 += 1
            continue
        else:
            break
result = count_2 if count_2 < count_5 else count_5
print(result)