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


# 3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
# (простое число - делится только на себя и 1)
# вход:
# 456
# 0
# вывод:
# 2^3 * 3 * 19
                

print("3. Break into simple multipliers")
entered=""
while True:
    try:
        entered = int(input("Enter a value to process it: "))
    except:
        print("Wrong input! Enter an integer value! (to exit enter '0')")
        continue
    if entered == 0:
        break
    divisors = []
    finished = False
    cur_val = entered
    col = len(str(entered)) 
    while finished == False:
        for x in range(2, cur_val+1):
            if cur_val % x == 0  and x < cur_val:
                print('{:>{w}} | {:<{w}}'.format(cur_val, x, w=col)) #в столбик
                divisors.append(x)
                cur_val //= x
                break
            elif x == cur_val:
                print('{:>{w}} | {:<{w}}'.format(cur_val, x,w=col)) #в столбик
                print('{:>{w}} |'.format(1, w=col))      #в столбик
                divisors.append(x)
                #print('Simple multipliers are ', divisors) # список
                #print(' * '.join(map(str,divisors)), '=', entered) # список в строку
                power = 1
                string = ""
                for i in range(len(divisors)):
                    if i == 0:
                        string += "{}".format(divisors[i])
                        #print(string)
                        continue
                    elif divisors[i] == divisors[i-1]:
                        power +=1
                        if i == len(divisors)-1:
                            string = string +  " ^ {}".format(power+1)
                            break
                        continue
                    elif divisors[i] != divisors[i-1] and power == 1:
                        string = string + " * {}".format(divisors[i])
                        continue
                    elif divisors[i] != divisors[i-1] and power > 1:
                        string = string +  " ^ {} * {}".format(power,divisors[i])
                        power = 1
                        continue
                    else:
                        print('Something strange happened!')
                string += ' = {}'.format(entered)    
                
                print('Simple multipliers are ', string)
                
                finished = True
                break
                
