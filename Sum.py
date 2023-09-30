def Sum(first_matrix, second_matrix):
    if len(second_matrix[0]) > 1:
        for string in second_matrix:
            first_matrix.append(string)
    else:
        first_matrix.append(second_matrix)

    for line in range(len(first_matrix)):
        for el in range(len(first_matrix[line])):
            first_matrix[line][el] = str(first_matrix[line][el])

    return first_matrix