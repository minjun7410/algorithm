N = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))
min_oil = 1000000001
result = 0
for index in range(len(oil)-1):
    if min_oil > oil[index]:
        min_oil = oil[index]
    result += distance[index] * min_oil
print(result)