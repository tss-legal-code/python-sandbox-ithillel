task = """
1. Дан массив. Реализовать функцию которая будет 
переставлять 2 выбранных элемента списка местами. 

Функция должна иметь вид:
def swap(target_list, item_index1, item_index2).

"""

def swap (target_list, item_index1,item_index2):
    print("old target_list is: {}".format(target_list))
    print("swapping {} with {}".format(item_index1,item_index2))
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    print("new target_list is: {}".format(target_list))
    print()
l = [x for x in range(20)]

print(task)

swap(l, 0,19)

swap(l, 1,18)

