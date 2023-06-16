import copy
class Cell:
    def __init__(self):
        self.value = None
    def setValue(self,value):
        self.value = value
    def getValue(self):
        return self.value if self.value != None else "EMPTY"
def replaceCell(table, value1, value2):
    for i in range(1, 51):
        for j in range(1, 51):
            if table[i][j].getValue() == value1:
                table[i][j].setValue(value2)
def unmergeCell(table, cell, r, c):
    for i in range(1, 51):
        for j in range(1, 51):
            if r == i and c == j: pass
            elif table[i][j] == cell:
                table[i][j] = Cell()
                
            
                
def solution(commands):
    answer = []
    table = [[Cell() for _ in range(51)] for _ in range(51)]
    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE" and len(command) == 4:
            r = int(command[1])
            c = int(command[2])
            value = command[3]
            table[r][c].setValue(value)
        elif command[0] == "UPDATE" and len(command) == 3:
            value1 = command[1]
            value2 = command[2]
            replaceCell(table, value1, value2)
        elif command[0] == "PRINT":
            r = int(command[1])
            c = int(command[2])
            answer.append(table[r][c].getValue())
        elif command[0] == "MERGE":
            r1 = int(command[1])
            c1 = int(command[2])
            r2 = int(command[3])
            c2 = int(command[4])
            cell1 = table[r1][c1]
            cell2 = table[r2][c2]
            if cell1 == cell2: continue
            elif cell1.getValue() == "EMPTY" and cell2.getValue() != "EMPTY":
                for i in range(1, 51):
                    for j in range(1, 51):
                        if table[i][j] == cell1:
                            table[i][j] = cell2
            else:
                for i in range(1, 51):
                    for j in range(1, 51):
                        if table[i][j] == cell2:
                            table[i][j] = cell1
        elif command[0] == "UNMERGE":
            r = int(command[1])
            c = int(command[2])
            unmergeCell(table, table[r][c], r, c)
        for i in range(1, 5):
            for j in range(1, 5):
                print(table[i][j].getValue(), end=" ")
            print()
    return answer
    