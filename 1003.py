array = [[0, 0] for _ in range(41)]
rep = int(input())

def fibonacci(n): #dynamic programming
    if array[n] != [0, 0]:
        return array[n]
    array1 = fibonacci(n-1)
    array2 = fibonacci(n-2)
    array[n][0] = array1[0] + array2[0]
    array[n][1] = array1[1] + array2[1]
    return array[n]

for i in range(rep):
    n = int(input())
    array[0] = [1, 0]
    array[1] = [0, 1]
    answer = fibonacci(n)
    print(answer[0], answer[1])
    
'''일반적인 방법 -> 오래걸림
def fibonacci(n):
    global zero, one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for r in range(rep):
    n = int(input())
    zero = one = 0
    fibonacci(n)
    print(zero, one)
    continue
   ''' 