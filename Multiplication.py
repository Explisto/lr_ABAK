def sub(first_matrix, second_matrix):
  answer = []

  for sign in range(3):

    if (first_matrix[sign] == 1 and second_matrix[sign] == 0) or (first_matrix[sign] == 0 and second_matrix[sign] == 1):
      return f"0 - пустая строка"

    elif first_matrix[sign] == '-' and second_matrix[sign] == '-':
      answer.append('-')

    elif (first_matrix[sign] == 1 and second_matrix[sign] == '-') or (first_matrix[sign] == '-' and second_matrix[sign] == 1):
      answer.append(1)

    elif (first_matrix[sign] == 0 and second_matrix[sign] == '-') or (first_matrix[sign] == '-' and second_matrix[sign] == 0):
      answer.append(0)

    else:
      answer.append(first_matrix[sign] and second_matrix[sign])

  return answer