# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Подзадание 1 (из 6):
# Дана строка “spam and eggs or eggs with spam”. Посчитать сколько раз встретился каждый символ.

s = 'spam and eggs of eggs with spam'

print("Дана строка: \'{}\'".format(s))
print("Строка состоит из {} символов".format(len(s)))

d ={}

for x in s:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1


print("Уникальных символов: ", len(d))

for x, y in sorted(d.items()):
    print("Символ \'{}\' встречается {} раз".format(x, y))