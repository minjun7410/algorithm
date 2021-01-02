def recursion(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]
    elif a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return recursion(20, 20, 20)
    elif a < b and b < c:
        one = recursion(a, b, c-1)
        dp[(a, b, c-1)] = one
        two = recursion(a, b-1, c-1)
        dp[(a, b-1, c-1)] = two
        three = recursion(a, b-1, c)
        dp[(a, b-1, c)] = three
        return one + two - three
    else:
        one = recursion(a-1, b, c)
        dp[(a-1, b, c)] = one
        two = recursion(a-1, b-1, c)
        dp[(a-1, b-1, c)] = two
        three = recursion(a-1, b, c-1)
        dp[(a-1, b, c-1)] = three
        four = recursion(a-1, b-1, c-1)
        dp[(a-1, b-1, c-1)] = four
        return one + two + three - four


dp = {}
while True:
    tmp = tuple(map(int, input().split()))
    if tmp == (-1, -1, -1):
        break
    a = tmp[0]
    b = tmp[1]
    c = tmp[2]
    print('w('+ str(a) + ', ' + str(b) + ', '+ str(c) + ') = '+ str(recursion(a, b, c))) 
    