# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Подзадание 3 (из 6):
# На ввод подается строка. Нужно узнать является ли строка палиндромом.
#(Палиндром - строка которая читается одинаково с начала и с конца.)

print("Testing strings on \'palindromness\'")
finish = False
while not finish:
    s = input("Enter string (type \'0\' to finish testing): ")
    if s == s[::-1]:
        print("String \'{}\' is a palindrom".format(s))
    else:
        print("String \'{}\' is NOT a palindrom".format(s))
    finish = True if s == "0" else False