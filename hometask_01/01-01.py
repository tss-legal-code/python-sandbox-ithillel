# 1. дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
row = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print("1. Given list: ", row)
mn, mx = min(row), max(row)

# 1.1 найти максимум, минимум и их индексы в массиве
print('1.1. Min is:', mn)
print('1.1. Min indexes :', [x for x in range(len(row)) if row[x]==mn])
print('1.1. Max is:', mx)
print('1.1. Max indexes :', [x for x in range(len(row)) if row[x]==mx])

#1.2 найти три самых часто встречаемых элемента массива
frequencies = [(n,sum([1 for v in row if v==n])) for n in set(row)]
print('1.2. Most popular 3 values are (just from top of stack, otherwise there is only 3 levels of popularity, i.e. all values comply with rule): ',[n[0] for n in sorted(frequencies, key = lambda x : x[1], reverse=True)[0:3]])

#1,3  преобразовать в список где каждое значение будет встречаться только 1 раз
print("1.3. Lists")
# 1.3.1 порядок не сохранялся
print('1.3.1. Unique values are (in acsending order):', sorted(set(row)))

# 1.3.2 порядок сохранялся
print('1.3.2. Unique values are (in order of occurence):', [row[x] for x in range(len(row)) if row.index(row[x])==x]  )
