task = """
HW3. Maze
Найти кратчайший путь до выхода из лабиринта
Лабиринт в текстовом виде [text_maze].

Обозначения [в text_maze]:
Непроходимые участки - '1'.
Доступные участки - '0'.
Старт - ‘х’.
Финиш - ‘#’.
Весь периметр огражден стеной [т.е. "1"].
Гарантируется, что путь существует.

Алгоритм с помощью которого можно решить называется волновой или алгоритм Ли

Алгоритм:
1.1. Найти координаты старта и финиша
1.2. Завести словарь was в котором отмечать - какие клетки были добавлены в 
     очередь и из какой клетки мы в них попадали
1.3. was[(neighbour_x, neighbour_y)] = (current_x, currnet_y)
1.4. Добавить в очередь стартовую координату. И отметить её в was.
1.5. Пока очередь не пуста - доставать из неё клетки, и добавлять соседей клетки если они доступны.
1.6. Если по ходу обхода мы встретим финишную клетку - значит путь найден можно выходить из цикла.
1.7. Используя was раскрутить путь от конечной точки до начала.
"""

print("{:=^80s}".format("< Найти кратчайший путь до выхода из лабиринта >"))
print("0. Setting initial variables")
maze_as_text = """111111111111111111
1x0010000000000001
111011101111111101
101010000100000001
101011010101111111
101000010100001001
100011110101111101
101110010100000001
100000000101101111
101101111100100001
101001000000101001
101101111111101001
101000000000001001
101011110100101001
101000010111111001
111011110100000001
101000000101111111
101011110101010101
1000000101000000#1
111111111111111111"""
print("1. \'maze_as_text\' is:\n{}".format(maze_as_text))

chars = {"wall": ("1",u"\u2588"),
         "path": ("0",""),
         "start": ("x",u"\u25b2"),
         "finish": ("#", u"\u2605"),
         "cell_width": 4}
print("2. \'chars\' dictionary is: {}".format(chars))

maze = {"start":"",
        "finish":"",
        "height": len(maze_as_text.split("\n")),
        "width": len(maze_as_text.split("\n")[0])}
print("3. \'maze\' initial dictionary is: {}".format(maze))

print("4. Create 'maze_as_list' + find start an finish char\'s coordinates")
maze_as_list = []
for y in range(maze["height"]):
    maze_as_list.append([])
    for x in range(maze["width"]):
        maze_as_list[y].append([])
        maze_as_list[y][x] = maze_as_text.split("\n")[y][x]
        if maze_as_list[y][x] == chars["start"][0]:
            maze["start"] = (y,x)
        if maze_as_list[y][x] == chars["finish"][0]:
            maze["finish"] = (y,x)
print("5. \'maze\' updated dictionary is: {}".format(maze))
print("6. Start coordinates are {} and finish coordinates are {}".format(maze["start"],maze["finish"]))

print("7. Make function to nicely view \'maze_as_list\' + display initial \'maze_as_list\'")

def view(trajectory=""):
    if trajectory:
        for y in range(maze["height"]):
            for x in range(maze["width"]):
                if (y,x) in trajectory and (y,x) !=  maze["start"] and (y,x) != maze["finish"]:
                    print("{:^{wd}}".format(trajectory.index((y,x)), wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["wall"][0]:
                    print("{:^{wd}}".format(chars["wall"][1] * chars["cell_width"], wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["path"][0]:
                    print("{:^{wd}}".format(chars["path"][1], wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["start"][0]:
                    print("{:^{wd}}".format(chars["start"][1], wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["finish"][0]:
                    print("{:^{wd}}".format(chars["finish"][1], wd=chars["cell_width"]), end="")
                else:
                    print("{:^{wd}}".format(maze_as_list[y][x], wd=chars["cell_width"]), end="")
            print()
    else:
        for y in range(maze["height"]):
            for x in range(maze["width"]):
                if maze_as_list[y][x] == chars["wall"][0]:
                    print("{:^{wd}}".format(chars["wall"][1]*chars["cell_width"],wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["path"][0]:
                    print("{:^{wd}}".format(chars["path"][1],wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["start"][0]:
                    print("{:^{wd}}".format(chars["start"][1],wd=chars["cell_width"]), end="")
                elif maze_as_list[y][x] == chars["finish"][0]:
                    print("{:^{wd}}".format(chars["finish"][1],wd=chars["cell_width"]), end="")
                else:
                    print("{:^{wd}}".format(maze_as_list[y][x],wd=chars["cell_width"]), end="")
            print()

view()

print("8. Finding shortest way in \'maze_as_list\' from start to finish")

was={maze["start"]:maze["start"]}
queue = [maze["start"]]
found = False

while not found:
    popped = queue.pop(0)
    y, x = popped
    new_cells = []
    for test_y, test_x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if (test_y, test_x) not in was and\
                (maze_as_list[test_y][test_x] == chars["path"][0] or maze_as_list[test_y][test_x] == chars["finish"][0]):
            new_cells.append((test_y, test_x))
    for i in new_cells:
        queue.append(i)
        was[i] = popped
        if maze_as_list[i[0]][i[1]] == chars["finish"][0]:
            found = True

#[print(item) for item in was.items()]

print("10. Restoring shortest way in \'maze_as_list\' from start to finish + view way")

trajectory = [maze["finish"]]
restored = False
while not restored:
    current = trajectory[0]
    if current == maze["start"]:
        restored = True
    else:
        for next_one, previous_one in was.items():
            if next_one == current:
                trajectory.insert(0,previous_one)
#print(trajectory)
view(trajectory)