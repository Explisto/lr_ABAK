def Neg():

    str_line = ['-', 1, 0]
    column = len(str_line)
    row = column - str_line.count("-")
    new_str = str_line.copy().remove("-")

    index = []
    pos = 0

    ans = [([0] * column) for i in range(row)]

    for i in range(column):
        if isinstance(str_line[i], int):
            index.append((pos, i))
            pos += 1

    for i in range(row):
        for j in range(column):
            if (i, j) in index:
                ans[i][j] = int(not str_line[j])
            else:
                ans[i][j] = '-'