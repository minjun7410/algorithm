N = int(input())
count = [[] for _ in range(50 +1)]
for _ in range(N):
    tmp = input()
    if tmp in count[len(tmp)]: #중복 없에기
        continue
    count[len(tmp)].append(tmp)
for i in count:
    i.sort()
    for j in i:
        print(j)