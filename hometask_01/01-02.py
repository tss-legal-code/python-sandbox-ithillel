#2 даны два словаря
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
print('2. Given 2 dicts')
print("a: ",a)
print("b: ",b)

#2.1 найти ключи которые есть в обоих словарях
print('2.1. Common keys are: ', set(a) & set(b))
#2.2 найти ключи которые есть только во 2м словаре, но нет в 1м
print('2.2. Keys only in "b" are: ', set(b) - set(a))

#2.3 объединить словари в один, так чтоб числа при одинаковых ключах суммировались
c = a.copy()
c.update(b)
for x in set(a) & set(b):
    c[x]=a[x]+b[x]
print("2.3. Merged dicts with summarised values of common keys: ", c)
