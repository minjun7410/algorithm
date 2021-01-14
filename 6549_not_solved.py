def divide_conquer(histogram, n):  # (list, height)
    global max_value
    if len(histogram) == 1:  # 길이가 1일 때는 더이상 분할할 일이 없으므로 끝내준다.
        max_value = histogram[0] if histogram[0] > max_value else max_value
        return
    for i in range(len(histogram)):  # 
        if histogram[i] == n:
            divide_conquer(histogram[0:i], n)
            divide_conquer(histogram[i+1:], n)
            return
    result = len(histogram) * n
    max_value = result if result > max_value else max_value
    divide_conquer(histogram[:], n+1)
    return


while True:
    histogram = list(map(int, input().split()))
    N = histogram[0]
    if N == 0:
        break
    histogram = histogram[1::]
    max_value = 0
    divide_conquer(histogram, 0)