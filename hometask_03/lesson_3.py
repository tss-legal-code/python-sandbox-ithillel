t = """111111111111111111
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

wall = u"\u2588"
path = " "
start_char = u"\u25b2"
end_char = u"\u2605"

t = t.replace("1", wall)
t = t.replace("0", path)
t = t.replace("x", start_char)
t = t.replace("#", end_char)

t = t.split("\n")



m =[]

for y in range(len(t)):
    m.append([])
    for x in range(len(t[0])):
        m[y].append([])
        m[y][x] = t[y][x]

def view():
    wd = 5
    for y in range(len(t)):
        for x in range(len(t[0])):
            if m[y][x] == start_char:
                print("{:^{wd}}".format(m[y][x],wd=wd), end="")
            elif m[y][x] == end_char:
                print("{:^{wd}}".format(m[y][x],wd=wd), end="")
            elif m[y][x] == wall:
                print(m[y][x]*wd,end ="")
            else:
                print("{:^{wd}}".format(m[y][x],wd=wd), end="")
        print()

view()

#everywhere coords format is: (y,x) ==> 'y' = row and 'x' = column

searched_cells = []
ways = (path, end_char)

def search_ways(cell):
    global searched_cells
    searched_cells.append(cell)
    y = cell[0]
    x = cell[1]

    return_ways = []
    for test_y, test_x in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
        if (test_y, test_x) not in searched_cells and m[test_y][test_x] in ways:
            return_ways.append((test_y, test_x))

    return return_ways



way = [(1,1)]

found_exit = False

while not found_exit:
    for c in way:
        for coords in search_ways((c[0], c[0])):
            print(coords)
    break


# while True
#     if len(stack) == 0:
#         cell = (1,1)
#
#     y = coords[0]
#     x = coords[1]
#
#     stack.append((coords))
#     print(coords, end ="")


# print()
#
# stack =[]
#
# def search(coords,
#            labirinth=m,
#            target=end_char,
#            free=path,
#            visited="X"):
#
#     #for storing path points we use 'stack'
#     global stack
#
#     # coords - for current position coords y(h):x(w)
#     y = coords[0]
#     x = coords[1]
#     stack.append((coords))
#     print(coords, end ="")
#
#     #detect target or if not detected - just mark current position and continue
#     if labirinth[y][x] == target:
#         return stack
#     else:
#         labirinth[y][x] = visited
#
#         if labirinth[y][x-1] != free and\
#            labirinth[y][x+1] != free and\
#            labirinth[y+1][x] != free and\
#            labirinth[y-1][x] != free:
#             stack = stack.remove((coords))
#
#         if labirinth[y-1][x] == free:
#             search((y - 1, x))
#
#         if labirinth[y+1][x] == free:
#             search((y + 1, x))
#
#         if labirinth[y][x+1] == free:
#             search((y, x + 1))
#
#         if labirinth[y][x-1] == free:
#             search((y, x - 1))
#
#
#
# trek = search((1, 1))
# print(trek)
# view()

##
##def search(coords,
##           labirinth=m,
##           target=end_char,
##           free=path,
##           visited="X"):
##
##    #for storing path points we use 'stack'
##    global stack
##
##    # coords - for current position coords y(h):x(w)
##    y = coords[0]
##    x = coords[1]
##    stack.append((coords))
##    
##    #detect target or if not detected - just mark current position and continue
##    if labirinth[y][x] == target:
##        return stack
##    else:
##        labirinth[y][x] = visited
##        if labirinth[y-1][x] == free:
##            return search((y - 1, x))
##        elif labirinth[y+1][x] == free:
##            return search((y + 1, x))
##        elif labirinth[y][x+1] == free:
##            return search((y, x + 1))
##        elif labirinth[y][x-1] == free:
##            return search((y, x - 1))
##        elif labirinth[y][x-1] != free and\
##           labirinth[y][x-1] != free and\
##           labirinth[y+1][x] != free and\
##           labirinth[y-1][x] != free:
##            return stack[:-1]
##
##trek = search((1, 1))
##print(trek)
##view()



##def go(cur):
##    # cur - for current coords y(h):x(w)
##    global val
##    y = cur[0]
##    x = cur[1]
##    m[y][x] = val
##    val +=1
##    if m[y-1][x] == path:
##        go((y - 1, x))
##    if m[y+1][x] == path:
##        go((y + 1, x))
##    if m[y][x+1] == path:
##        go((y, x + 1))
##    if m[y][x-1] == path:
##        go((y, x - 1))
