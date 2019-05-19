# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Подзадание 6 (из 6):
# Дана строка "English = 78 Science = 83 Math = 68 History = 65". Вычислить сумму всех чисел в строке.

print("Value summarizer")

s = "English = 78.22 Science = 83 Math = 68 History = 65"
print("Given string is: {}".format(s))

s_sum = 0

for x in s.split():
    x = x.strip()
    try:
        print("adding {} to {}".format(eval(x), s_sum))
        s_sum += eval(x)
    except:
        pass

print("sum of numbers in a string is: {}".format(s_sum))



