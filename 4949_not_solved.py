while True:
    string = input()
    if string[0] == '.':
        break 
    big = []
    small = []
    result = "yes"
    #  [([]])
    for char in string:
        if char == '[':
            big.append('[')
        elif char == ']':
            if len(big) == 0  or (small and small[-1] == '('):
                result = "no"
                break
            else:
                big.pop()
        elif char == '(':
            small.append('(')
        elif char == ')':
            if len(small) == 0 or (big and big[-1] == '['):
                result = "no"
                break
            else:
                small.pop()
        else:
            continue
    if len(big) != 0 or len(small) != 0:
        result = "no"
    print(result)