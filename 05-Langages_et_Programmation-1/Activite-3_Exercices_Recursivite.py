""" Exerice 1 (Calcul des lignes du triangle de pascal) """


def pascal_triangle_line(n):
  if n == 0:
    return [1]
  else:
    previous_line = pascal_triangle_line(n-1)
    line = [1]
    for i in range(len(previous_line)-1):
      line.append(previous_line[i] + previous_line[i+1])
    line.append(1)
    return line

for i in range(5):
  print(pascal_triangle_line(i))
