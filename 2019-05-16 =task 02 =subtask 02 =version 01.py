# Домашнее задание 2
# Добавлено: 17.05.2019 20:02
# Базовые типы данных. Условный оператор и циклы
# Необязательное подзадание 2 (из 6):
# Дан отсортированный массив, реализуйте бинарный поиск

#make random incremental list
from random import randint

lst = [x for x in range(1,1000,randint(1,100))]

print("list is: ",lst)

print('Max index: ', len(lst)-1)

value = randint(1,1000)

print("Searched value is: ",value)

print()

index_width = len(str(len(lst))) #for index formatting
value_width = len(str(lst[-1]))  #for values formatting

#initial boundaries
left=0
right=len(lst)-1
mid = (right - left) // 2

result = None

while result == None:

    if right-left == 1 or\
       value < lst[left] or\
       value > lst[right]:
        result = 'not found'
        print("Value {} is not found in array".format(value) )
        break
        
    if value == lst[left]:
        result = left
        break
    elif value == lst[mid]:
        result = mid
        break
    elif value == lst[right]:
        result = right
        break
    elif value < lst[mid]:
        right = mid
        mid = (right - left) // 2 + left
        shifting = "<<< set \'right\' to \'middle\' <<<"
    elif value > lst[mid]:
        left = mid
        mid = (right - left) // 2 + left
        shifting = "<<< set \'left\'  to \'middle\' <<<"
    #view current results of calculations
    print("Left[{:>{iw}}]={:<{vw}}, middle[{:>{iw}}]={:<{vw}}, right[{:>{iw}}]={:<{vw}} {}"\
          .format(left,lst[left], mid,lst[mid], right,lst[right],shifting, iw=index_width,vw=value_width))

print("\nResult's index is ",result)
