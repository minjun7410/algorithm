many = int(input())
factors = list(map(int, input().split()))
max_value = 0
min_value = 987654321
for i in range(many):
    if max_value < factors[i]:
        max_value = factors[i]
    if min_value > factors[i]:
        min_value = factors[i]
print(max_value * min_value)