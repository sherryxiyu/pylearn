lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista.remove('b')
print(lista)
lista.pop(4)
print(lista)
del lista[-1]
print(lista)

lista.append(['help', 'repair'])
print(lista)
lista = lista + [1, 2, 3]
print(lista)
lista.extend([4, 4, 4])
print(lista)

lista[1] = 'second'
print(lista)

a = lista[6]
print(a)

dicta = {'first': 1, 'second': 2, 'third': 3, 4: 'four', 'listb': [5, 6, 7]}
dicta.update({'five': 5, 'six': 6})
print(dicta)
dicta['first'] = 'how are you?'
print(dicta)
dicta[5] = 'this is six'
print(dicta)

b = dicta.get('haha', 0)
print(b)

c = dicta.values()
print(c)
d = dicta.keys()
print(d)
e = dicta.items()
print(e)

f = dicta.pop('listb')
print(f)
print(dicta)
g = dicta.popitem()
print(g)
print(dicta)

b = [('b', 8), ('a', 5), ('n', 3), ('y', 7), ('5', 2), ('o', 8)]
b = sorted(b, key=lambda x: x[0])
print(b)
c = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(c)

e = [i ** 2 for i in [2, 3, 4, 5]]
print(e)
# 字典生成式:https://blog.csdn.net/qdPython/article/details/129346307
f = {k: v for k, v in zip([2, 3, 4], [5, 6, 7])}
print(f)