import ast

data = input().strip()
if not data.startswith("["):
    data = "[" + data + "]"
matrix = list(ast.literal_eval(data))
matrix.sort(key=lambda x: x[1])
print(matrix)