task = """
2. Дан массив целых чисел. 

Нужно найти сумму элементов с индексами, у которых сумма бит двоичного представления четна 

[т.е. ищем "элементы", у которых сумма бит двоичного представления их "индексов" четна, 
      и суммируем эти "элементы"]. 
    
Затем перемножить эту сумму и предпоследний элемент исходного массива

"""
print(task)
a = [x for x in range(1,25,3)]
print("Array is: {}\n".format(a))


sum_items = 0
for x in range(len(a)):
    print("Element \'{} \'has index \'{}\' with binary representation \'{}\'".format(a[x],x, bin(x)[2:]  ))
    if sum([int(n) for n in bin(x)[2:]]) % 2 == 0:
        sum_items+=a[x]
        print("FOUND! Adding {}, current sum is {}".format(a[x], sum_items))
else:
    print("\nsearch complete, current sum is {}".format(sum_items))

print("\nSum of items with \'special\' indexes is \'{}\'\npenultimate element is \'{}\'\n\
if we multipy this sum with penultimate element we get \'{}\'".format(sum_items,a[-2], sum_items*a[-2]))

