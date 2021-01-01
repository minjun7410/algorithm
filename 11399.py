N = int(input())
lst = list(map(int, input().split()))
lst.sort()
sums = lst[0]
dynamic = lst[0]
for index in range(1, N):
    dynamic += lst[index]
    sums += dynamic
print(sums)
