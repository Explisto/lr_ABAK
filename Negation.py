from Multiplication import sub_matrix
def negation(line):
  column = len(line)

  if "-" in line:
    row = column - line.count("-")
    new_str = line.copy().remove("-")
  else:
    row = column

  index = []
  pos = 0

  ans = [(["0"]*column) for i in range(row)]

  for i in range(column):
    if line[i] != "-":
      index.append((pos, i))
      pos += 1

  for i in range(row):
    for j in range(column):
      if (i, j) in index:
        ans[i][j] = str(int(not int(line[j])))
      else:
        ans[i][j] = "-"

  return ans

def neg_matrix(matrix):

  res = negation(matrix[0]) # получили отрицательную строчку

  # идём по остальной матрице
  for el in range(1, len(matrix)):
    temp = negation(matrix[el])
    # если результат умножения Матрица
    if isinstance(temp[0], list):
      res = sub_matrix(res, temp)
    else:
      res = sub_matrix(temp, res)

  return res