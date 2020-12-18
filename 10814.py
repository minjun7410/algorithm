N = int(input())
count = [[] for _ in range(200 + 1)]
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    count[age].append(name)
for i in range(1, 200 + 1):
    for j in count[i]:
        print(i, j)