
def sub(s1, s2):
  answer = []

  for sign in range(len(s1)):
    if (s1[sign] == '1' and s2[sign] == '0') or (s1[sign] == '0' and s2[sign] == '1'):
      return f"0 - пустая строка"
    elif s1[sign] == '-' and s2[sign] == '-':
      answer.append('-')
    elif (s1[sign] == '1' and s2[sign] == '-') or (s1[sign] == '-' and s2[sign] == '1'):
      answer.append('1')
    elif (s1[sign] == '0' and s2[sign] == '-') or (s1[sign] == '-' and s2[sign] == '0'):
      answer.append('0')
    else:
      answer.append(s1[sign] and s2[sign])

  return answer



def sub_matrix(m1, m2):

  out = list()  # результат

  for row1 in m1:
    for row2 in m2:
    # если результат умножения строк это 0
      if (res := sub(row1, row2)) == "0 - пустая строка":
        continue
      out.append(res)
  # если список не пустой
  if out:
    return out
  else:
    return [["0 - пустая строка"]]