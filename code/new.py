import ast
dictionary = ast.literal_eval("{'a': 1, 'b': 2}")
print (type(dictionary))
print (dictionary)

x = 10
print(ast.parse("x+19"))

