# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Подзадание 5 (из 6):
# Напишите генератор случайных паролей.
# После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
# Завершить программу нужно если будет введен 0.
# Также нужно проверять является ли введенная строка числом.
# Допустимые символы - цифры, большие и маленькие латинские буквы.

from string import ascii_letters
from string import digits
from random import choice

print("Password generator")
c = digits + ascii_letters
print("dictionary of chars is: {}".format(c))

while True:
    try:
        n = int(input("Enter length of password (type \'0\' to end program): "))
    except:
        print("Enter an integer value!!!")
        continue
    if n == 0: break

    password = ""
    for x in range (n):
        password += choice(c)


    print("Randomly generated password is:\n\n{}\n".format(password))




