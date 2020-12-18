N = int(input())
start = 666
lst = [0, 666]
if len(lst) -1 == N: 
    print(lst[N])
else:
    while True:
        start += 1
        tmp = str(start)
        if '666' in tmp:
            lst.append(tmp)
        if len(lst) - 1 == N:
            print(lst[-1])
            break