def sum_3(i, j, k):
    global min_value
    tmp = 0
    for index in range(4):
        if i[index] != j[index]:
            tmp += 1
        if j[index] != k[index]:
            tmp += 1
        if i[index] != k[index]:
            tmp += 1
    if tmp < min_value:
        min_value = tmp
    return


T = int(input())

for _ in range(T):
    N = int(input())
    
    min_value = 100000000
    lst = list(input().split())
    dic = {}
    for case in lst:
        if case not in dic:
            dic[case] = 1
        else:
            dic[case] += 1
    key = dic.keys()
    for i in key:
        dic[i] -= 1
        for j in key:
            if dic[j] == 0:
                continue
            dic[j] -= 1
            for k in key:
                if dic[k] == 0:
                    continue
                sum_3(i, j, k)
            dic[j] += 1
        dic[i] += 1
    print(min_value)