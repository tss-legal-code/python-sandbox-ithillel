def swap (target_list, item_index1,item_index2):
    print("old target_list is: {}".format(target_list))
    print("swapping {} with {}".format(item_index1,item_index2))
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    print("new target_list is: {}".format(target_list))
    print()
l = [x for x in range(40)]

swap(l, 10,20)

swap(l, 20,39)

