import json
a={
			'name':'tushar',
			'age':19,
			'mrk':[90,87,75],
}
b=json.dumps(a)
print(type(b))
print(b)
print(a['name'])
