n, m = map(int, input().split())

def get_zero(n):
    count_2 = 0
    count_5 = 0
    
    tmp = 2
    while n >= tmp:  # 1 2(1) 3 4(2) 5 6(1) 7 8(3) 9 10(1) 11 12(2) 13 14(1) 15 16(4) 17 18(1) 19 20(2) 21 22(1) 23 24(3) 25     2, 4, 8, 16 ~ 이렇게 2의 제곱근으로 나누어지는 수(n // 2(or 4, 8)) count + 1을 한다.
        count_2 += n // tmp
        tmp *= 2
    
    tmp = 5
    while n >= tmp:  # 1 2 3 4 5(1) 6 7 8 9 10(1) 11 12 13 14 15(1) 16 17 18 19 20(1) 21 22 23 24 25(2)         
        count_5 += n // tmp
        tmp *= 5
    
    return count_2, count_5
two, five = get_zero(n)
two_2, five_2 = get_zero(m)
two_3, five_3 = get_zero(n-m)

result = min(two-(two_2+two_3), five-(five_2+five_3))
print(result)