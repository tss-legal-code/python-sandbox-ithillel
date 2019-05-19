# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Подзадание 4 (из 6):
# На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться.

#########################################################
# Ниже приведено два решения.
# первое реализовано если делить "слова" только по пробелам
# второе - можно (интерактивно) настроить под нужды пользователя, в первую очередь чтоб отделить "слова" от "пунктуации"
#########################################################

# первое решение
print("{:=^80s}".format("< Primitive solution >"))
s = "На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться."
print("from string: ", end = "")
print(s)
print("we get:      ", end = "")
for x in s.split():
    print(x[::-1], end =" ")
print("\n")

# второе решение
print("{:=^80s}".format("< More interesting solution (^_^) >"))

d = (" ", ",", ".") 
verbose_output = False

print("Reversing every word in a given string")
print("Current set of word delimiters is: {}".format(d))
print("Verbose output", "enabled" if verbose_output else "disabled")


def split_by_delimiter(s,d):
    """
    reverse string splitted into "words" by a specified delimiter set
    s - for given string
    d - for given delimiters
    """

    if verbose_output:
        print ("Current set of word delimiters is: {}".format(d))
        print ("string      :", end="")
        for x in range(len(s)):
            print('{:^4}'.format(s[x]),end="")
        print()    
        print ("indexes     :", end="")
        for x in range(len(s)):
            print('{:^4}'.format(x),end="")
        print()
        

    split_indexes=[]

    if verbose_output: print ("split points:", end="")

    for x in range(len(s)):
        if x == 0:
            split_indexes.append(0)
        if s[x] in d:
            split_indexes.append(x)
            if verbose_output:
                print('{:^4}'.format('\u25b2'),end="")
        else:
            if verbose_output:
                print('{:^4}'.format(""),end="")
        if x == len(s)-1:
            split_indexes.append(len(s))
        

    if verbose_output: print()

    i_pairs = []
    i_prev = split_indexes[0]
    i_next = split_indexes[1]
    
    for x in range(1,len(split_indexes)+1):
        if x <  len(split_indexes):
            i_pairs.append((i_prev,i_next))
            i_prev, i_next = i_next + 1, split_indexes[x]
        elif x ==  len(split_indexes):
            i_pairs.append((i_prev,i_next))
            i_prev, i_next = i_next + 1, len(s)-1
        else:
            i_pairs.append((i_prev,i_next))
        
    result = s 
    for x in range(len(i_pairs)):
        result = result.replace(result[i_pairs[x][0]:i_pairs[x][1]],\
                                result[i_pairs[x][0]:i_pairs[x][1]][::-1],\
                                1)
    
    print("from string: \'{}\'".format(s))
    print("we get:      \'{}\'".format(result))
    

while True:
    s = input("Enter string (\'0\' - to end program, \'1\' - to edit delimiters, \'2\' - to tun on/off verbose ouput ): ")
    if s == "0":
        print("Program terminated!")
        break
    if s == "1":
        s = input("Enter a few one-symbol delimiters: ")
        d = list(set(s))
        print ("Current set of word delimiters is: {}".format(d))
        continue
    if s == "2":
        verbose_output = not verbose_output
        print("Verbose output", "enabled" if verbose_output else "disabled")
        continue
    else:
        split_by_delimiter(s,d)
        
