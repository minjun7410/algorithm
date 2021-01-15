import sys
sys.setrecursionlimit(300000)
def divide_conquer(start, end):  # (list, height)
    global max_value
    if start == end:
        max_value = histogram[start] if histogram[start] > max_value else max_value
        return
    min_index = start
    min_value = histogram[start]
    for i in range(start, end+1):
        if histogram[i] < min_value:
            min_index = i
            min_value = histogram[i]
    area = min_value * (end - start + 1)
    max_value = area if area > max_value else max_value
    
    if start == min_index:
        divide_conquer(min_index+1, end)
    elif end == min_index:
        divide_conquer(start, min_index-1)
    else:
        divide_conquer(start, min_index-1)
        divide_conquer(min_index+1, end)
    return
    


while True:
    histogram = list(map(int, sys.stdin.readline().split()))
    N = histogram[0]
    if N == 0:
        break
    histogram = histogram[1:]
    max_value = 0
    
    divide_conquer(0, len(histogram)-1)
    print(max_value)