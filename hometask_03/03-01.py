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

def view(lab):
    wd = 5
    for y in range(len(lab)):
        for x in range(len(lab[0])):
            if lab[y][x] == start_char:
                print("{:^{wd}}".format(lab[y][x],wd=wd), end="")
            elif lab[y][x] == end_char:
                print("{:^{wd}}".format(lab[y][x],wd=wd), end="")
            elif lab[y][x] == wall:
                print(lab[y][x]*wd,end ="")
            else:
                print("{:^{wd}}".format(lab[y][x],wd=wd), end="")
        print()


m =[]
start_coords = ()
end_coords = ()

for y in range(len(t)):
    m.append([])
    for x in range(len(t[0])):
        m[y].append([])
        m[y][x] = t[y][x]
        if m[y][x] == start_char:
            start_coords = (y,x)
        if m[y][x] == end_char:
            end_coords = (y,x)



print("1. Coordinates for start are {} and for finish are {}".format(start_coords,end_coords))

step = 0

current_cell = [start_coords]
next_cell=[]

found = False
final_coords = ()

while not found:
    step += 1
    next_cell = []
    for coords in current_cell:
        #print("step {} coords {}".format(step, coords))
        y, x = coords
        if m[y][x] == end_char:
            print("Python found exit!!!")
            m[y][x] = step
            final_coords = (y,x)
            found = True
        else:
            m[y][x] = step
        for test_y, test_x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if m[test_y][test_x] == path or m[test_y][test_x] == end_char:
                next_cell.append((test_y, test_x))

    current_cell = next_cell

view(m)

for i in range(step):
    y, x  = final_coords
    m[y][x] = "#"
    for test_y, test_x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if m[test_y][test_x] == step - 1:
            m[test_y][test_x] = "#"
            final_coords = (test_y,test_x)
            step-=1

for y in range(len(m)):
    for x in range(len(m[0])):
        if isinstance(m[y][x],int):
            m[y][x] = ""


print()
view(m)

