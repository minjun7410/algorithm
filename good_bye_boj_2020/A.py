N = int(input())
lst = list(input().split())
boolean = True
head = []
tail = []
for i in range(N):
    for j in range(len(lst[i])):
        if len(lst[i]) == 1:
            head.append(lst[i][0])
            tail.append(lst[i][-1])
            if head[0] != lst[i][0] or tail[0] != lst[i][0]:
                boolean = False
            break
        if j == len(lst[i])-j-1 or j + 1 == len(lst[i])-j-1:
            head.append(lst[i][0])
            tail.append(lst[i][-1])
            if head[0] != lst[i][0] or tail[0] != lst[i][-1]:
                boolean = False
            break
        if lst[i][j] != lst[i][len(lst[i])-j-1]:
            boolean = False
            break
    if not(boolean):
        break
if not(boolean):
    print(0)
else:
    print(1)