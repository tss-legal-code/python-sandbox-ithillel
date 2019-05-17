# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Подзадание 4 (из 6):
# На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться.

#start work
print("Reversing every word in a given string (words are splitted by space \' \' )")

#single reversion

s = "На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться."
print("from string: ", end = "")
print(s)
print("we get:      ", end = "")
for x in s.split():
    print(x[::-1], end =" ")
print("\n"*2)


#looping game
while True:
    s = input("Enter string (type \'0\' to finish messing words around): ").strip()
    if s == "0": break    
    print("from string: ", end = "")
    print(s)
    print("we get:      ", end = "")
    
    for x in s.split():
        print(x[::-1], end =" ")
    print("\n"*2)
