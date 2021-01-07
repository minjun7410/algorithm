while True:
    string = input()
    if string[0] == '.':
        break 
    bracket = []
    result = "yes"
    #  [()[]]
    for value in string:
        if value == '[':
            bracket.append('[')
        elif value == '(':
            bracket.append('(')
        elif value == ']':
            if len(bracket) == 0:
                result = 'no'
                break
            for i in range(len(bracket)-1, -1, -1):
                if bracket[i] == '(':
                    result = 'no'
                    break
                elif bracket[i] == '[':
                    del bracket[i]
                    break
            if result == 'no':
                break
        elif value == ')':
            if len(bracket) == 0:
                result = 'no'
                break
            for i in range(len(bracket)-1, -1, -1):
                if bracket[i] == '[':
                    result = 'no'
                    break
                elif bracket[i] == '(':
                    del bracket[i]
                    break
            if result == 'no':
                break
        else:
            continue
    if len(bracket) != 0:
        result = 'no'
    print(result)
                